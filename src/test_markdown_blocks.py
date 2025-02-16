import unittest
from markdown_blocks import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_blocks(self):
        sample_text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        expected_ouput = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertListEqual(expected_ouput, markdown_to_blocks(sample_text))
    

    def test_markdown_blocks_extra_lines(self):
        sample_text = """# This is a heading




This is a paragraph of text. It has some **bold** and *italic* words inside of it.





* This is the first list item in a list block
* This is a list item
* This is another list item"""





        expected_ouput = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertListEqual(expected_ouput, markdown_to_blocks(sample_text))

    def test_markdown_blocks_empty_markdown(self):
            sample_text = ""

            expected_ouput = []
            self.assertListEqual(expected_ouput, markdown_to_blocks(sample_text))
    
    
    