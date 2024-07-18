import unittest
from block_markdown import markdown_to_blocks, block_to_block_type


class TestTextNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
