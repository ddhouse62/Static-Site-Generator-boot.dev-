from enum import Enum
from htmlnode import ParentNode, LeafNode
from text_to_textnode import text_to_textnode
from textnode import TextNode, text_node_to_html_node, TextType
# Takes a raw markdown string (representing a full document).
# returns a list of 'block strings

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block != "":
            new_blocks.append(block.strip())
    return new_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

# TODO - Finish Markdown to HTML Node function
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_nodes.append(block_to_html_node(block, block_type))
    return ParentNode("div", block_nodes)


        

def text_to_children(text):
    text_nodes = text_to_textnode(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            text = block.replace("\n", " ").strip()
            children = text_to_children(text)
            return ParentNode("p", children)
        
        case BlockType.HEADING:
            heading_level = block.split()[0].count('#')
            text = block.split(" ", 1)[1].strip()
            children = text_to_children(text)
            return ParentNode(f"h{heading_level}", children)
        
        case BlockType.CODE:
            text_lines = block.splitlines()
            del text_lines[0]
            del text_lines[-1]
            text = "\\n".join(text_lines).strip()
            text_node = TextNode(text, TextType.TEXT)
            children = text_node_to_html_node(text_node)
            code_block = ParentNode("code", [children])
            return ParentNode("pre", [code_block])
        
        case BlockType.QUOTE:
            text_lines = block.splitlines()
            text_lines_no_formatter = []
            for line in text_lines:
                text_lines_no_formatter.append(line.split(" ", 1)[1].strip())
            text = "\n".join(text_lines_no_formatter)
            children = text_to_children(text)
            return ParentNode("blockquote", children)
        
        case BlockType.UNORDERED_LIST:
            text_lines = block.splitlines()
            list_items = []
            for line in text_lines:
                text = line.split(" ", 1)[1].strip()
                children = text_to_children(text)
                list_items.append(ParentNode("li", children))
            return ParentNode("ul", list_items)
        
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for i in range(len(lines)):
                text = lines[i].split(" ", 1)[1].strip()
                children = text_to_children(text)
                list_items.append(ParentNode(f"{i + 1}", children))
            return ParentNode("ol", list_items)

        case _:
            raise Exception(f"Valid BlockType required.  You submitted {block_type}")






                            