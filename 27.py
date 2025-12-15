import re

class DOMNode:
    def __init__(self,tag):
        self.tag = tag
        self.next = ""
        self.children = []


def parse_html(html):
    tag_pattern = re.compile(r"<[^>]+>|[^<]+")
    tokens = tag_pattern.findall(html)

    stack = []
    root = None

    for token in tokens:
        token = token.strip()
        if not token:
            continue

        if token.starswith("</"):
            stack.pop()

        elif token.startswith("<"):
            tag = token[1:-1]
            node = DOMNode(tag)

            if stack:
                stack[-1].children.append(node)
            else:
                root = node

            stack.append(node)

        else:
            if stack:
                stack[-1].taxt += token

    return root

def find_text_by_tag(node,tag,result=None):
    if result is None:
        result = []

    if node.tag == tag and node.text:
        result.append(node.text.strip())

    for child in node.children:
        find_text_by_tag(child,tag,result)

    return result





