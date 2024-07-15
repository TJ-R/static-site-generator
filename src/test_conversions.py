import unittest

from textnode import TextNode
from htmlnode import LeafNode
from conversions import text_node_to_leaf_node


class TestConversions(unittest.TestCase):
    def test_text_to_leaf(self):
        node = TextNode("This is a text node", "text")
        correct_leaf = LeafNode(None, "This is a text node")

        result = text_node_to_leaf_node(node)

        self.assertEqual(result.tag, correct_leaf.tag)
        self.assertEqual(result.value, correct_leaf.value)
        self.assertEqual(result.props, correct_leaf.props)

    def test_bold_to_leaf(self):
        node = TextNode("This is a text node", "bold")
        correct_leaf = LeafNode("b", "This is a text node")

        result = text_node_to_leaf_node(node)

        self.assertEqual(result.tag, correct_leaf.tag)
        self.assertEqual(result.value, correct_leaf.value)
        self.assertEqual(result.props, correct_leaf.props)

    def test_italic_to_leaf(self):
        node = TextNode("This is a text node", "italic")
        correct_leaf = LeafNode("i", "This is a text node")

        result = text_node_to_leaf_node(node)

        self.assertEqual(result.tag, correct_leaf.tag)
        self.assertEqual(result.value, correct_leaf.value)
        self.assertEqual(result.props, correct_leaf.props)

    def test_code_to_leaf(self):
        node = TextNode("This is a text node", "code")
        correct_leaf = LeafNode("code", "This is a text node")

        result = text_node_to_leaf_node(node)

        self.assertEqual(result.tag, correct_leaf.tag)
        self.assertEqual(result.value, correct_leaf.value)
        self.assertEqual(result.props, correct_leaf.props)

    def test_link_to_leaf(self):
        node = TextNode("This is a text node", "link", "www.testingurl.com")
        correct_leaf = LeafNode("a", "This is a text node", {"href": "www.testingurl.com"})

        result = text_node_to_leaf_node(node)

        self.assertEqual(result.tag, correct_leaf.tag)
        self.assertEqual(result.value, correct_leaf.value)
        self.assertEqual(result.props, correct_leaf.props)

    def test_image_to_leaf(self):
        node = TextNode("This is a test", "image", "www.testingurl.com")
        correct_leaf = LeafNode("img", "", {"src": "www.testingurl.com", "alt": "This is a test"})

        result = text_node_to_leaf_node(node)

        self.assertEqual(result.tag, correct_leaf.tag)
        self.assertEqual(result.value, correct_leaf.value)
        self.assertEqual(result.props, correct_leaf.props)


if __name__ == "__main__":
    unittest.main()
