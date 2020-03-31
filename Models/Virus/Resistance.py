from Exceptions.BadArgumentFormat import BadArgumentFormat
import xml.etree.ElementTree as xml
class Resistance:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__from=root.attrib['from']
        self.__to=root.attrib['to']
    def __str__(self):
        return f"Virus could survive {self.__name} in values {self.__from}-{self.__to}"
