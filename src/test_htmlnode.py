import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
    attribute_href,
    attribute_target 
)

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "Hello world!")
        node2 = HTMLNode("h1", "abcd", [node], {attribute_href: "https://google.com"})
        self.assertEqual(
            "HTMLNode(h1, abcd, [HTMLNode(p, Hello world!, None, None)], {'href': 'https://google.com'})",
                node2.__repr__() 
        )
        
    def test_props_to_html(self):
        node = HTMLNode("h1", "abcd", None, 
                        {attribute_href: "https://google.com", attribute_target: "_blank"})
        self.assertEqual(" href=\"https://google.com\" target=\"_blank\"", node.props_to_html())
        
class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("h1", "abcd", {attribute_href: "https://google.com"})
        self.assertEqual(
            "LeafNode(h1, abcd, {'href': 'https://google.com'})", node.__repr__()
        )
        
    def test_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())
    
    def test_to_html_a(self):
        node = LeafNode("a", "Click me!", {attribute_href: "https://www.google.com"})
        self.assertEqual(
            "<a href=\"https://www.google.com\">Click me!</a>", node.to_html()
        )
        
    def test_to_html_a_no_props(self):
        node = LeafNode("a", "Click me!", None)
        self.assertEqual(
            "<a>Click me!</a>", node.to_html()
        )

class TestParentNode(unittest.TestCase):
    def test_repr(self):
        node = ParentNode("h1", [], {attribute_href: "https://www.google.com"})
        self.assertEqual(
            "ParentNode(h1, [], {'href': 'https://www.google.com'})", node.__repr__()
        )
    
    def test_to_html_one_leaf_node(self):
        node = ParentNode("h1", [LeafNode("p", "Hello world!")], 
                          {attribute_href: "https://www.google.com"})
        self.assertEqual(
            "<h1 href=\"https://www.google.com\"><p>Hello world!</p></h1>", node.to_html()
        )
    
    def test_to_html_multiple_leaf_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())
        
        
    def test_to_html_multiple_leaf_nodes_and_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "h1", 
            [
                LeafNode("p", "Hello world!"),
                node
            ], 
            {attribute_href: "https://www.google.com"})
        self.assertEqual(
            "<h1 href=\"https://www.google.com\"><p>Hello world!</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></h1>",
            node2.to_html()
        )
