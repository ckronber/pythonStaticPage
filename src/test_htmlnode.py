import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        test_prop= {"href": "https://www.google.com","target": "_blank"}
        html_node1 = HTMLNode("p","This is some text",None,test_prop)
        self.assertEqual("href=\"https://www.google.com\" target=\"_blank\"",html_node1.props_to_html())

    def test_props2(self):
        test_prop= {"href": "https://www.facebook.com","target": "_blank"}
        html_node1 = HTMLNode("p","This is some text",None,test_prop)
        self.assertEqual("href=\"https://www.facebook.com\" target=\"_blank\"",html_node1.props_to_html())
    
    def test_props3(self):
        test_prop= {"href": "https://www.twitter.com","target": "_blank"}
        html_node1 = HTMLNode("p","This is some text",None,test_prop)
        self.assertEqual("href=\"https://www.twitter.com\" target=\"_blank\"",html_node1.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Click Me!",{"href":"https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_parent_node_to_html(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text")])
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")


if __name__ == "main":
    unittest.main()