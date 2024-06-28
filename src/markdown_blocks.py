import re
from htmlnode import *
from textnode import *
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = [s.strip() for s in markdown.split('\n\n')]
    return [b for b in blocks if b]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            nodes.append(paragraph_to_html_node(block))
        if block_type == block_type_heading:
            nodes.append(heading_to_html_node(block))
        if block_type == block_type_code:
            nodes.append(code_to_html_node(block))
        if block_type == block_type_quote:
            nodes.append(quote_to_html_node(block))
        if block_type == block_type_unordered_list:
            nodes.append(unordered_list_to_html_node(block))
        if block_type == block_type_ordered_list:
            nodes.append(ordered_list_to_html_node(block)) 
    return ParentNode("div", nodes)


def block_to_inline_html_nodes(block):
    return [text_node_to_html_node(tn) for tn in text_to_textnodes(block)]
    
def paragraph_to_html_node(block):
    return ParentNode("p", block_to_inline_html_nodes(block.replace('\n', ' ')))

def heading_to_html_node(block):
    level = len(re.match(r'^#{1,6}', block).group())
    return ParentNode(f"h{level}", block_to_inline_html_nodes(block[level+1:]))

def code_to_html_node(block):
    return ParentNode("pre", [ParentNode("code", block_to_inline_html_nodes(block))])

def quote_to_html_node(block):
    block.split('\n')
    quote = ' '.join([q[2:] for q in block.split('\n') if q.startswith('> ')])
    return ParentNode("blockquote", block_to_inline_html_nodes(quote))

def unordered_list_to_html_node(block):
    items = [i[2:] for i in block.split('\n')]
    item_nodes = []
    for item in items:
        item_nodes.append(ParentNode("li", block_to_inline_html_nodes(item)))
    return ParentNode("ul", item_nodes)

def ordered_list_to_html_node(block):
    items = [i[3:] for i in block.split('\n')]
    item_nodes = []
    for item in items:
        item_nodes.append(ParentNode("li", block_to_inline_html_nodes(item)))
    return ParentNode("ol", item_nodes)

def block_to_block_type(block):
    lines = block.split('\n')

    if block.startswith('#') and re.findall(r'^#{1,6} ', block):
        return block_type_heading
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    if block.startswith('> '):
        for line in lines[1:]:
            if not line.startswith('> '):
                return block_type_paragraph
        return block_type_quote
    if block.startswith('* ') or block.startswith('- '):
        return block_type_unordered_list
    if block.startswith('1. '):
        for i, line in enumerate(lines[1:], 1):
            if not line.startswith(f'{i+1}. '):
                return block_type_paragraph
        return block_type_ordered_list
    return block_type_paragraph