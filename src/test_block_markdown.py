import unittest
from block_markdown import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()
