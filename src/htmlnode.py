attribute_href = "href"
attribute_target = "target"

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> None:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        attributes = ""
        if self.props:
            for key, value in self.props.items():
                attributes += f" {key}=\"{value}\""
        return attributes.rstrip(' ')
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.tag}, {self.children}, {self.props})"