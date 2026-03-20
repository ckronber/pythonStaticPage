from enum import Enum
from htmlnode import LeafNode

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class TextType(Enum):
    BOLD = "b"
    ITALIC = "i"
    TEXT = None
    CODE = "code"
    LINK = "a href"
    IMAGE = "img"

class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,TextNode):
        return self.text == TextNode.text and self.text_type == TextNode.text_type and self.url == TextNode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self,TextNode):
        if TextNode is None:
            raise Exception
        else:
            return LeafNode(TextNode.text_type,TextNode.text,TextNode.url)