from parse_markdown import (split_nodes_delimiter, split_nodes_image, split_nodes_link)
from textnode import (TextNode, TextType)

def text_to_textnode(text):
    text_node = [TextNode(text, TextType.TEXT)]
    split_node_code = split_nodes_delimiter(text_node, '`', TextType.CODE)
    split_node_bold = split_nodes_delimiter(split_node_code, "**", TextType.BOLD)
    split_node_italic = split_nodes_delimiter(split_node_bold, "*", TextType.ITALIC)
    split_node_images = split_nodes_image(split_node_italic)
    final_split = split_nodes_link(split_node_images)
    return final_split
    