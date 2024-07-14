import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is text node 1.", "bold")
        node2 = TextNode("This is text node 2.", "bold")
        self.assertNotEqual(node, node2)

    def test_different_text_types(self):
        node = TextNode("This is a text node.", "bold")
        node2 = TextNode("This is a text node.", "italic")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
