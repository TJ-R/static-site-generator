import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html, extract_title


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):
        markdown = """
# This is a heading

This is a paragraph of text.
It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = markdown_to_blocks(markdown)

        self.assertListEqual(
                [
                    "# This is a heading",
                    "This is a paragraph of text.\nIt has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                ],
                result
        )

    def test_markdown_to_blocks_newlines(self):
        markdown = """
# This is a heading




This is a paragraph of text.
It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = markdown_to_blocks(markdown)

        self.assertListEqual(
                [
                    "# This is a heading",
                    "This is a paragraph of text.\nIt has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                ],
                result
        )

    def test_block_to_blocktype_paragraph(self):
        block = "This is just some random text"
        expected = "paragraph"

        result = block_to_block_type(block)

        self.assertEqual(expected, result)

    def test_block_to_blocktype_heading(self):
        block = "### This is a heading"
        expected = "heading"

        result = block_to_block_type(block)

        self.assertEqual(expected, result)

    def test_block_to_blocktype_code(self):
        block = "``` This is a code block ```"
        expected = "code"

        result = block_to_block_type(block)

        self.assertEqual(expected, result)

    def test_block_to_blocktype_quote(self):
        block = ">Quote Line 1\n>Quote Line 2"
        expected = "quote"

        result = block_to_block_type(block)

        self.assertEqual(expected, result)

    def test_block_to_blocktype_unordered_list(self):
        block = "* Line 1\n- Line 2"
        expected = "unordered_list"

        result = block_to_block_type(block)

        self.assertEqual(expected, result)

    def test_block_to_blocktype_ordered_list(self):
        block = "1. Line 1\n2. Line 2"
        expected = "ordered_list"

        result = block_to_block_type(block)

        self.assertEqual(expected, result)

    def test_paragraph_to_html(self):
        markdown = "this is a **paragraph**"

        result = markdown_to_html(markdown)

        self.assertEqual(result.to_html(), "<div><p>this is a <b>paragraph</b></p></div>")

    def test_code_to_html(self):
        markdown = "```This is the code in a code block```"
        result = markdown_to_html(markdown)

        self.assertEqual(result.to_html(), "<div><pre><code>This is the code in a code block</code></pre></div>")

    def test_heading_to_html(self):
        markdown = """
# this is an h1

## this is an h2
"""
        result = markdown_to_html(markdown)

        self.assertEqual(result.to_html(), "<div><h1>this is an h1</h1><h2>this is an h2</h2></div>")

    def test_unordered_list_to_html(self):
        markdown = """
- This is a unordered list
- with multiple items
"""

        result = markdown_to_html(markdown)

        self.assertEqual(result.to_html(), "<div><ul><li>This is a unordered list</li><li>with multiple items</li></ul></div>")

    def test_ordered_list_to_html(self):
        markdown = """
1. This is a ordered list
2. with multiple items
"""

        result = markdown_to_html(markdown)

        self.assertEqual(result.to_html(), "<div><ol><li>This is a ordered list</li><li>with multiple items</li></ol></div>")

    def test_block_quote_to_html(self):
        markdown = """
> This is a block quote
> with multiple lines
"""

        result = markdown_to_html(markdown)
        self.assertEqual(result.to_html(), "<div><blockquote>This is a block quote with multiple lines</blockquote></div>")

    def test_extract_title(self):
        markdown = "# Hello"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")


if __name__ == "__main__":
    unittest.main()
