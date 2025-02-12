from htmlnode import *
from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_nodes = node.text.split(delimiter)
            if len(split_nodes) % 2 == 0:
                raise ValueError("Invalid Markdown, formatted section not closed")
            for i in range(len(split_nodes)):
                if split_nodes[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_nodes[i], text_type))
                    
    return new_nodes


def extract_markdown_images(text):
    extracted_images = (re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"), text)
    return extracted_images

def extract_markdown_links(text):
    extracted_links = (re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"), text)
    return extracted_links