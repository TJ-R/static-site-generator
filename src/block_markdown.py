import re
from htmlnode import ParentNode
from conversions import text_node_to_leaf_node
from inline_markdown import text_to_textnodes


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


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    root = ParentNode("div", [])

    for block in blocks:
        block_type = block_to_block_type(block)
        new_html_node = None

        if block_type == "heading":
            header_level, header_text = block.split(' ', 1)
            new_html_node = createHeaderNode(
                header_level.count("#"), header_text)
        elif block_type == "code":
            new_html_node = createCodeNode(block)
        elif block_type == "quote":
            new_html_node = createQuoteNode(block)
        elif block_type == "unordered_list":
            new_html_node = createUnorderedListNode(block)
        elif block_type == "ordered_list":
            new_html_node = createOrderedListNode(block)
        else:
            new_html_node = createParagraphNode(block)

        root.children.append(new_html_node)

    return root


def createHeaderNode(level, text):
    header_node = ParentNode(f"h{level}", [])
    child_nodes = text_to_children(text)
    header_node.children.extend(child_nodes)
    return header_node


def createCodeNode(block):
    pre_node = ParentNode("pre", [])
    code_node = ParentNode("code", [])

    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")

    text = block[3:-3]
    child_nodes = text_to_children(text)

    code_node.children.extend(child_nodes)
    pre_node.children.append(code_node)

    return pre_node


def createQuoteNode(block):
    block_quote_node = ParentNode("blockquote", [])
    lines = []
    for line in block.split("\n"):
        lines.append(line.split(' ', 1)[1])
    text = " ".join(lines)
    children = text_to_children(text)
    block_quote_node.children.extend(children)

    return block_quote_node


def createUnorderedListNode(block):
    ul_node = ParentNode("ul", [])

    for line in block.split("\n"):
        li_node = ParentNode("li", [])
        text = line.split(' ', 1)[1]
        children = text_to_children(text)
        li_node.children.extend(children)
        ul_node.children.append(li_node)

    return ul_node


def createOrderedListNode(block):
    ol_node = ParentNode("ol", [])

    for line in block.split("\n"):
        li_node = ParentNode("li", [])
        text = line.split(' ', 1)[1]
        children = text_to_children(text)
        li_node.children.extend(children)
        ol_node.children.append(li_node)

    return ol_node


def createParagraphNode(block):
    paragraphNode = ParentNode("p", [])
    children = text_to_children(block)
    paragraphNode.children.extend(children)
    return paragraphNode


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_leaf_node(text_node))
    return children


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == "heading":
            header_level, header_text = block.split(' ', 1)
            if header_level.count("#") == 1:
                return header_text.strip()

    raise ValueError("Could not find title in markdown")
