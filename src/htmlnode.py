class HTML_Node():
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
        stringVAl = ""
        for key,val in self.props.items():
            stringVAl+= f" {prop.key}={prop.val}"

        return stringVAl