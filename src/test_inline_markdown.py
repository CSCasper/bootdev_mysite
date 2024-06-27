import unittest

from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text)
            ], new_nodes
        )
    
    def test_split_nodes_delimiter_at_start(self):
        node = TextNode("`code block` at the front", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("code block", text_type_code),
                TextNode(" at the front", text_type_text)
            ], new_nodes
        )
    
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word and here's another `code block too`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word and here's another ", text_type_text),
                TextNode("code block too", text_type_code),
            ], new_nodes
        )
    
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        self.assertListEqual([("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")], 
                          extract_markdown_images(text))
        
    def test_extract_markdown_images_multi(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)" \
            "and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        self.assertListEqual([("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
                          ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")], 
                          extract_markdown_images(text))

    def test_extract_markdown_images_empty(self):
        text = ""
        self.assertListEqual([], extract_markdown_images(text))
    
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com)"
        self.assertListEqual([("link", "https://www.example.com")],
                         extract_markdown_links(text))
    
    def test_extract_markdown_links_multi(self):
        text = "This is text with a [link](https://www.example.com)" \
            "and [another](https://www.example.com/another)"
        self.assertListEqual([("link", "https://www.example.com"), 
                          ("another", "https://www.example.com/another")],
                         extract_markdown_links(text))
        
    def test_extract_markdown_links_empty(self):
        text = ""
        self.assertListEqual([], extract_markdown_links(text))

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)" \
            " and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")],
            new_nodes
            )

    def test_split_nodes_image_start(self):
        node = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)" \
            " and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")],
            new_nodes
            )
        
    def test_split_nodes_link_empty(self):
        node = TextNode("", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com)" \
            " and [another](https://www.example.com/another)",
            text_type_text
            )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_link, "https://www.example.com/another")],
            new_nodes)

    def test_split_nodes_link_start(self):
        node = TextNode(
            "[link](https://www.example.com)" \
            " and [another](https://www.example.com/another)",
            text_type_text
            )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_link, "https://www.example.com/another")],
            new_nodes
            )

    def test_split_nodes_link_empty(self):
        node = TextNode("", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
        
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an " \
                "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a " \
                "[link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev")
            ],
            new_nodes
        )
    
    def test_text_to_textnodes_link_first(self):
        text = "[link](https://boot.dev) This is **text** with an *italic* word and a `code block` and an " \
                "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a " \
                "[link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        
        self.assertListEqual(
            [
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev")
            ],
            new_nodes
        )
    
    def test_text_to_textnodes_image_first(self):
        text = "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) This is **text** with an *italic* word and a `code block` and an " \
                "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a " \
                "[link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev")
            ],
            new_nodes
        )

tester = TestInlineMarkdown()
tester.test_text_to_textnodes()