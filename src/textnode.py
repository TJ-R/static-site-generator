from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode2):
        if (self.text == textNode2.text
            and self.text_type == textNode2.text_type
                and self.url == textNode2.url):
            return True

        else:
            return False

    def __repr__(self):
        print(f'TextNode({self.text}, {self.text_type}, {self.url})')
