from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"

class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,TextNode):
        return self.text == TextNode.text and self.text_type == TextNode.text_type and self.url == TextNode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"