from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
def main():
    new_node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
    
    

    node1 = HTMLNode("tag", "value", ["child1", "child2"], {"prop": "https://boot.dev", "prop2": "https://example.com"})
    

    node2 = LeafNode("a", "Value1", {"href": "https://google.com"})
    node2.to_html()
    
    parent_node = ParentNode("p", [node2, LeafNode("b", "Click Here"), ParentNode("a", [LeafNode("i", "Value2")])])
    #print(parent_node.to_html())

    print(text_node_to_html_node(new_node).to_html())
    

main()