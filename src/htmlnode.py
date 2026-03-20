class HTMLNode():
    def __init__(self,tag:str=None,value:str=None,children:list=None,props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"Tag:{self.tag} Value:{self.value} Children:{self.children} Props:{self.props}"
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_str = ""
        for key,val in self.props.items():
            props_str+= f" {key}=\"{val}\""
        return props_str.strip()


class LeafNode(HTMLNode):
    def __init__(self,tag:str,value:str,props:dict=None):
        super().__init__(tag=tag,value=value,props=props)
    
    def __repr__(self):
        return f"Tag:{self.tag} Value:{self.value} Props:{self.props}"

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return self.value
        else:
            if self.props is not None:
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children:list,props=None):
        super().__init__(tag=tag,children=children,props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("")
        if self.children is None:
            raise ValueError([])

        leaf_vals = ""
        for child in self.children:
            leaf_vals += child.to_html()
        return f"<{self.tag}>{leaf_vals}</{self.tag}>"