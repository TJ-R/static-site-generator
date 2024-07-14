

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""

        html = ""
        for key, value in self.props.items():
            html += f" {key}=\"{value}\""

        return html

    def __repr__(self):
        print(f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})')


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Node has no value")

        if self.tag is None:
            return self.value

        prop_html = self.props_to_html()

        return f"<{self.tag}" + prop_html + ">" + self.value + f"</{self.tag}>"

    def __repr__(self):
        print(f'LeafNode({self.tag}, {self.value}, {self.props})')


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: Tag cannot be none")
        if self.children is None:
            raise ValueError("Error: Children cannot be none")

        prop_html = self.props_to_html()

        child_html = ""

        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}" + prop_html + ">" + child_html + f"</{self.tag}>"
