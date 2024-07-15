from textnode import TextNode


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
