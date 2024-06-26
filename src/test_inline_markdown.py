import unittest

from inline_markdown import (
    split_nodes_delimiter
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text)
            ], new_nodes
        )
    
    def test_split_nodes_delimiter_at_start(self):
        node = TextNode("`code block` at the front", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            [
                TextNode("code block", text_type_code),
                TextNode(" at the front", text_type_text)
            ], new_nodes
        )
    
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word and here's another `code block too`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word and here's another ", text_type_text),
                TextNode("code block too", text_type_code),
            ], new_nodes
        )