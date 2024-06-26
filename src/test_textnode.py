import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a textnode", text_type_bold)
        node2 = TextNode("This is a textnode", text_type_bold)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a textnode - 1", text_type_bold)
        node2 = TextNode("This is a textnode - 2", text_type_bold)
        self.assertNotEqual(node, node2)
        
    def test_not_eq_text_type(self):
        node = TextNode("This is a textnode", text_type_bold)
        node2 = TextNode("This is a textnode", text_type_italic)
        self.assertNotEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a textnode", text_type_bold, "https://mysite.net")
        node2 = TextNode("This is a textnode", text_type_bold, "https://mysite.net")
        self.assertEqual(node, node2)
        
    def test_not_eq_no_url(self):
        node = TextNode("This is a textnode", text_type_bold)
        node2 = TextNode("This is a textnode", text_type_bold, "https://mysite.net")
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()