from xml.sax.handler import ContentHandler
from xml.sax import parse


class TestHandler(ContentHandler):

    in_headline = False

    def __init__(self, headlines):
        super().__init__()
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        # 跟踪当前解析的文本是否位于一对h1标签内
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            # 跟踪当前解析的文本是否位于一对h1标签内
            self.in_headline = False

    def characters(self, string):
        if self.in_headline:
            self.data.append(string)


headlines = []
parse('website.xml', TestHandler(headlines))

print('The following <h1> elements were found:')
for h in headlines:
    print(h)