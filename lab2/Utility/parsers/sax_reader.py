import xml.sax as sax


class XmlReader(sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.table_data = []
        self.stock_data = []
        self.parser = sax.make_parser()

    def startElement(self, name, attrs):
        """
        Rewritten function from inherited class which use as start parser element
        :param name: current element name
        :param attrs: attributes (don't used)
        :return: None
        """
        self.current = name
        if name == "stock":
            pass

    def characters(self, content) -> None:
        """
        Also rewritten function that perform getting data characters
        :param content: character
        :return: None
        """
        if self.current == "name":
            self.name = content
        elif self.current == "line_up":
            self.line_up = content
        elif self.current == "position":
            self.position = content
        elif self.current == "titles":
            self.titles = content
        elif self.current == "street":
            self.street = content

    def endElement(self, name) -> None:
        """
        Rewritten function from inherited class which use as end parser element
        :param name:
        :return: None
        """
        if self.current == "name":
            self.stock_data.append(self.name)
        elif self.current == "line_up":
            self.stock_data.append(self.line_up)
        elif self.current == "position":
            self.stock_data.append(self.position)
        elif self.current == "titles":
            self.stock_data.append(self.titles)
        elif self.current == "street":
            self.stock_data.append(self.street)
        if len(self.stock_data) == 5:
            self.table_data.append(tuple(self.stock_data))
            self.stock_data = []

        self.current = ""
