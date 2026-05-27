import os
import shutil

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse_markdown import *
from text_to_textnode import text_to_textnode
from markdown_blocks import *
from website import copy_static

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)



main()