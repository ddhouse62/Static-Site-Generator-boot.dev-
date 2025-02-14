from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse_markdown import *
from text_to_textnode import text_to_textnode
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

    sample_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    resulting_nodes = text_to_textnode(sample_text)
    for node in resulting_nodes:
        if node.text_type == TextType.LINK or node.text_type == TextType.IMAGE:
            print(f"TextNode(\"{node.text}\", {node.text_type}, \"{node.url}\"),")
        else:

            print(f"TextNode(\"{node.text}\", {node.text_type}),")





main()