import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_unequal(self):
        node = TextNode("This is a text node2", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_equal_type(self):
        node = TextNode("This is a text node2", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_type, node2.text_type)

    def test_notEqual_type(self):
        node = TextNode("This is a text node2", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag.value, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag.value, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code_text(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag.value, "code")
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()