import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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




class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "Click Here", {"href": "google.com"})
        test_response = ("<a href=\"google.com\">Click Here</a>")
        
        self.assertEqual(node.to_html(), test_response)

    
    def test_no_tag(self):
        node = LeafNode(None, "value", None)
        self.assertEqual(node.to_html(), "value")

    def test_repr(self):
        node = LeafNode("a", "value", {"prop": "prop_val"})
        self.assertEqual("Tag: a, Value: value, Children: None, Props: {\'prop\': \'prop_val\'}", repr(node))



class TestParentNode(unittest.TestCase):
    def test_to_html_1_child(self):
        node = ParentNode("p", [LeafNode("a", "Click Here", {"href": "google.com"})])
        self.assertEqual(node.to_html(), "<p><a href=\"google.com\">Click Here</a></p>")

    
if __name__ == "__main__":
    unittest.main()