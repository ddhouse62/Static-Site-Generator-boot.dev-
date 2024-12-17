import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node3 = TextNode("TryThis", TextType.CODE, "https://boot.dev")
        node4 = TextNode("TryThis", TextType.CODE, "https://boot.dev")
        self.assertEqual(node3, node4)

    def text_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")

        self.assertNotEqual(node, node5)

    def diff_text_type(self):
        node = TextNode("Testing diff text", TextType.ITALIC)
        node2 = TextNode("Testing diff text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def with_diff_url(self):
        node = TextNode("Test", TextType.CODE, "https://youtube.com")
        node2 = TextNode("Test", TextType.CODE, "https://google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()