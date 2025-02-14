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
    extracted_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_images

def extract_markdown_links(text):
    extracted_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_links


def split_nodes_image(old_nodes):    
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:

            node_text = node.text
            extracted_images = extract_markdown_images(node_text)
            if node_text == "":
                continue
            
            if len(extracted_images) == 0:
                new_nodes.append(node)
                continue
            
            else:
                
                for alt_text, link in extracted_images:

                    split_nodes = node_text.split(f"![{alt_text}]({link})", 1)

                    if len(split_nodes) != 2:
                        raise ValueError("Invalid Markdown, formatted section not closed")
            

                    if split_nodes[0] == "":
                        new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))
                        node_text = split_nodes[1]
                        continue

                    elif split_nodes[1] == "":

                        new_nodes.append(TextNode(split_nodes[0], TextType.TEXT))
                        new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))
                        node_text = ""
                        continue

                    else:
                        new_nodes.append(TextNode(split_nodes[0], TextType.TEXT))
                        new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))
                        node_text = split_nodes[1]
                        continue

                if len(node_text) > 0:
                    new_nodes.append(TextNode(node_text, TextType.TEXT))        
    return new_nodes


def split_nodes_link(old_nodes):    
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:

            node_text = node.text
            extracted_links = extract_markdown_links(node_text)
            if node_text == "":
                continue
            
            if len(extracted_links) == 0:
                new_nodes.append(node)
                continue
            
            else:
                
                for alt_text, link in extracted_links:

                    split_nodes = node_text.split(f"[{alt_text}]({link})", 1)

                    if len(split_nodes) != 2:
                        raise ValueError("Invalid Markdown, formatted section not closed")
            

                    if split_nodes[0] == "":
                        new_nodes.append(TextNode(alt_text, TextType.LINK, link))
                        node_text = split_nodes[1]
                        continue

                    elif split_nodes[1] == "":

                        new_nodes.append(TextNode(split_nodes[0], TextType.TEXT))
                        new_nodes.append(TextNode(alt_text, TextType.LINK, link))
                        node_text = ""
                        continue

                    else:
                        new_nodes.append(TextNode(split_nodes[0], TextType.TEXT))
                        new_nodes.append(TextNode(alt_text, TextType.LINK, link))
                        node_text = split_nodes[1]
                        continue

                if len(node_text) > 0:
                    new_nodes.append(TextNode(node_text, TextType.TEXT))        
    return new_nodes


    