from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    new_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(new_node)

    node1 = HTMLNode("tag", "value", ["child1", "child2"], {"prop": "https://boot.dev", "prop2": "https://example.com"})
    print(node1.props_to_html())

main()