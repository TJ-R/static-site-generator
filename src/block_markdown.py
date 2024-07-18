import re


def markdown_to_blocks(markdown):
    return list(
        filter(
            lambda x: x != "",
            map(lambda x: x.strip(), markdown.split("\n\n"))
            )
        )


def block_to_block_type(block):
    if is_heading(block):
        return "heading"
    elif is_codeblock(block):
        return "code"
    elif is_quote(block):
        return "quote"
    elif is_unordered_list(block):
        return "unordered_list"
    elif is_ordered_list(block):
        return "ordered_list"
    else:
        return "paragraph"


def is_heading(block):
    headings = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    return any(block.startswith(h) for h in headings)


def is_codeblock(block):
    return block.startswith("```") and block.endswith("```")


def is_quote(block):
    return all(line.startswith(">") for line in block.split("\n"))


def is_unordered_list(block):
    return all(line.startswith("* ") or line.startswith("- ") for line in block.split("\n"))


def is_ordered_list(block):
    return all(re.search(r"^\d+.\s", line) for line in block.split("\n"))
