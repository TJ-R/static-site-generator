import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "This is value", [], {"href": "https://www.google.com", "target": "_blank"})
        correct_html = " href=\"https://www.google.com\" target=\"_blank\""
        result_html = node.props_to_html()
        self.assertEqual(result_html, correct_html)

    def test_leaf_to_html(self):
        node = LeafNode("a", "This is value", {"href": "https://www.google.com", "target": "_blank"})
        correct_html = "<a href=\"https://www.google.com\" target=\"_blank\">This is value</a>"
        result_html = node.to_html()
        self.assertEqual(result_html, correct_html)

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Test")
        result = node.to_html()
        correct = "Test"
        self.assertEqual(result, correct)

    def test_parent_with_one_child_to_html(self):
        node = ParentNode("div", [LeafNode("b", "Bold Text")])
        correct_html = "<div><b>Bold Text</b></div>"
        result_html = node.to_html()
        self.assertEqual(result_html, correct_html)


if __name__ == "__main__":
    unittest.main()
