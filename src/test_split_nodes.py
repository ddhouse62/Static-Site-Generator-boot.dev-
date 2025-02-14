import unittest
from parse_markdown import (
    split_nodes_delimiter, split_nodes_image
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_image_split(self):
        test_node = TextNode(
        "![img1](link1) Middle text ![img2](link2).",
        TextType.TEXT
        )
        test_split_nodes = split_nodes_image([test_node])
        self.assertEqual(test_split_nodes, [TextNode("img1", TextType.IMAGE, "link1"), TextNode(" Middle text ", TextType.TEXT), TextNode("img2", TextType.IMAGE, "link2"), TextNode(".", TextType.TEXT)])

    def test_image_split_consecutive(self):
        node = TextNode(
        "![img1](link1)![img2](link2)",
        TextType.TEXT
        )
        test_split_nodes = split_nodes_image([node])
        self.assertListEqual(test_split_nodes, [TextNode("img1", TextType.IMAGE, "link1"), TextNode("img2", TextType.IMAGE, "link2")])

    def test_image_split_end(self):
        test_node = TextNode(
        "![img1](link1) Middle text ![img2](link2)",
        TextType.TEXT
        )
        test_split_nodes = split_nodes_image([test_node])
        self.assertListEqual(test_split_nodes, [TextNode("img1", TextType.IMAGE, "link1"), TextNode(" Middle text ", TextType.TEXT), TextNode("img2", TextType.IMAGE, "link2")])
    
    def test_image_split_trailing_text(self):
        test_node = TextNode(
        "![img1](link1) End text ",
        TextType.TEXT
        )
        test_split_nodes = split_nodes_image([test_node])
        self.assertListEqual(test_split_nodes, [TextNode("img1", TextType.IMAGE, "link1"), TextNode(" End text ", TextType.TEXT)])

    def test_image_split_empty_node(self):
        old_nodes = []
        self.assertListEqual(split_nodes_image(old_nodes), [])
    
    def test_image_split_no_text_in_textnode(self):
        test_node = TextNode("", TextType.TEXT)
        self.assertListEqual(split_nodes_image([test_node]), [])
    
    def test_image_split_non_text_old_nodes(self):
        old_nodes = [
            TextNode("Some text ![img1](link1)", TextType.TEXT), 
            TextNode("Don't touch this", TextType.LINK, "http://example.com")
        ]

        expected_output = [
            TextNode("Some text ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "link1"),
            TextNode("Don't touch this", TextType.LINK, "http://example.com")
        ]

        self.assertListEqual(split_nodes_image(old_nodes), expected_output)



if __name__ == "__main__":
    unittest.main()