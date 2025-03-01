from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse_markdown import *
from text_to_textnode import text_to_textnode
from markdown_blocks import *
def main():
    '''
    new_node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
    
    

    node1 = HTMLNode("tag", "value", ["child1", "child2"], {"prop": "https://boot.dev", "prop2": "https://example.com"})
    

    node2 = LeafNode("a", "Value1", {"href": "https://google.com"})
    node2.to_html()
    
    parent_node = ParentNode("p", [node2, LeafNode("b", "Click Here"), ParentNode("a", [LeafNode("i", "Value2")])])
    #print(parent_node.to_html())

    print(text_node_to_html_node(new_node).to_html())
    '''

    '''test_node = TextNode(
        "![img1](link1) Middle text ![img2](link2)",
        TextType.TEXT
    )
    test_split_nodes = split_nodes_image([test_node])
    for node in test_split_nodes:
        print(node.text)
    '''
    
    sample_markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

    print(markdown_to_blocks(sample_markdown))





main()