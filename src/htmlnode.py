

from multiprocessing import Value


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_string = ""

        for prop in self.props:
            prop_value = self.props[prop]
            props_string += f" {prop}=\"{prop_value}\""
        return props_string
    
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(value, tag, None, props)

    
    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"