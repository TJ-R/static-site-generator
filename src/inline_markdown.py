from textnode import TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == "text":
            split_string = node.text.split(delimiter)
            if len(split_string) % 2 == 0:
                raise ValueError("Text contains invalid markdown syntax")

            for i in range(len(split_string)):
                if split_string[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_string[i], "text"))
                else:
                    new_nodes.append(TextNode(split_string[i], text_type))
        else:
            new_nodes.append(node)

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if len(images) > 0:
            text = old_node.text
            for i in range(len(images)):
                alt_text = images[i][0]
                source_text = images[i][1]
                sections = text.split(f"![{alt_text}]({source_text})", 1)

                if (sections[0] != ""):
                    new_node = TextNode(sections[0], "text")
                    new_nodes.append(new_node)

                img_node = TextNode(alt_text, "image", source_text)
                new_nodes.append(img_node)

                # If its last image
                if i == (len(images) - 1):
                    if sections[1] != "":
                        new_node = TextNode(sections[1], "text")
                        new_nodes.append(new_node)
                else:
                    text = sections[1]

        else:
            new_nodes.append(old_node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if len(links) > 0:
            text = old_node.text
            for i in range(len(links)):
                link_text = links[i][0]
                source_text = links[i][1]
                sections = text.split(f"[{link_text}]({source_text})", 1)

                if (sections[0] != ""):
                    new_node = TextNode(sections[0], "text")
                    new_nodes.append(new_node)

                link_node = TextNode(link_text, "link", source_text)
                new_nodes.append(link_node)

                # If its last image
                if i == (len(links) - 1):
                    if sections[1] != "":
                        new_node = TextNode(sections[1], "text")
                        new_nodes.append(new_node)
                else:
                    text = sections[1]

        else:
            new_nodes.append(old_node)

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "*", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
