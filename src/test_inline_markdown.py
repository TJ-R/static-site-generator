import unittest

from textnode import TextNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


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

    def test_split_node_double_bold(self):
        node = TextNode("This is **bold** and make that **double**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, "text")

        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, "bold")

        self.assertEqual(new_nodes[2].text, " and make that ")
        self.assertEqual(new_nodes[2].text_type, "text")

        self.assertEqual(new_nodes[3].text, "double")
        self.assertEqual(new_nodes[3].text_type, "bold")

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

    def test_split_image(self):
        old_nodes = [TextNode("This is text with a ![rick roll](https://i.imgur.com/aKa0qIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg). This is extra.", "Text")]
        expected = [TextNode("This is text with a ", "text"), TextNode("rick roll", "image", "https://i.imgur.com/aKa0qIh.gif"),
                    TextNode(" and ", "text"), TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(". This is extra.", "text")]

        results = split_nodes_image(old_nodes)

        for i in range(len(expected)):
            self.assertEqual(results[i].text, expected[i].text)
            self.assertEqual(results[i].text_type, expected[i].text_type)
            self.assertEqual(results[i].url, expected[i].url)

    def test_split_link(self):
        old_nodes = [TextNode("This is text with a [rick roll](https://i.imgur.com/aKa0qIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg). This is extra.", "Text")]
        expected = [TextNode("This is text with a ", "text"), TextNode("rick roll", "link", "https://i.imgur.com/aKa0qIh.gif"),
                    TextNode(" and ", "text"), TextNode("obi wan", "link", "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(". This is extra.", "text")]

        results = split_nodes_link(old_nodes)

        for i in range(len(expected)):
            self.assertEqual(results[i].text, expected[i].text)
            self.assertEqual(results[i].text_type, expected[i].text_type)
            self.assertEqual(results[i].url, expected[i].url)

    def test_split_no_image_and_link(self):
        old_nodes = [TextNode("This has no img", "text")]
        expected = [TextNode("This has no img", "text")]

        results = split_nodes_image(old_nodes)

        for i in range(len(expected)):
            self.assertEqual(results[i].text, expected[i].text)
            self.assertEqual(results[i].text_type, expected[i].text_type)
            self.assertEqual(results[i].url, expected[i].url)

        results = split_nodes_link(old_nodes)

        for i in range(len(expected)):
            self.assertEqual(results[i].text, expected[i].text)
            self.assertEqual(results[i].text_type, expected[i].text_type)
            self.assertEqual(results[i].url, expected[i].url)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        results = text_to_textnodes(text)

        self.assertListEqual([
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),], results
        )


if __name__ == "__main__":
    unittest.main()
