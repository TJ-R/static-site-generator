import unittest

from textnode import TextNode
from helper import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestHelper(unittest.TestCase):
    def test_split_node_bold(self):
        node = TextNode("This is a **text** node", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[0].text_type, "text")

        self.assertEqual(new_nodes[1].text, "text")
        self.assertEqual(new_nodes[1].text_type, "bold")

        self.assertEqual(new_nodes[2].text, " node")
        self.assertEqual(new_nodes[2].text_type, "text")

    def test_split_node_error(self):
        node = TextNode("This is a **text node", "text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", "bold")

    def test_split_node_one_word(self):
        node = TextNode("**Test**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes[0].text, "Test")
        self.assertEqual(new_nodes[0].text_type, "bold")

    def test_split_multiple_nodes(self):
        node = TextNode("This is a *text* node", "text")
        node2 = TextNode("This is a *test*", "text")

        new_nodes = split_nodes_delimiter([node, node2], "*", "italic")
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[0].text_type, "text")

        self.assertEqual(new_nodes[1].text, "text")
        self.assertEqual(new_nodes[1].text_type, "italic")

        self.assertEqual(new_nodes[2].text, " node")
        self.assertEqual(new_nodes[2].text_type, "text")

        self.assertEqual(new_nodes[3].text, "This is a ")
        self.assertEqual(new_nodes[3].text_type, "text")

        self.assertEqual(new_nodes[4].text, "test")
        self.assertEqual(new_nodes[4].text_type, "italic")

    def test_split_node_non_text_type(self):
        node = TextNode("This is a **text** node", "bold")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes[0].text, "This is a **text** node")
        self.assertEqual(new_nodes[0].text_type, "bold")

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKa0qIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKa0qIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        results = extract_markdown_images(text)

        self.assertEqual(len(expected), len(results))

        for i in range(len(expected)):
            self.assertTupleEqual(results[i], expected[i])

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        results = extract_markdown_links(text)

        self.assertEqual(len(expected), len(results))

        for i in range(len(expected)):
            self.assertTupleEqual(results[i], expected[i])


if __name__ == "__main__":
    unittest.main()
