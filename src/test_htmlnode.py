import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        node = HTMLNode("tag", "value", ["child1", "child2"], {"prop1": "prop1val", "prop2": "prop2val"})
        test_response = (" prop1=\"prop1val\" prop2=\"prop2val\"")
        
        self.assertEqual(node.props_to_html(), test_response)

    
    def test_eq(self):
        node = HTMLNode("tag", None, ["child1", "child2"], None)
        node2 = HTMLNode("tag", None, ["child1", "child2"], None)
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_repr(self):
        node = HTMLNode("tag", "value", ["child"], {"prop": "prop_val"})
        self.assertEqual("Tag: tag, Value: value, Children: [\'child\'], Props: {\'prop\': \'prop_val\'}", repr(node))