from Exceptions.BadArgumentFormat import BadArgumentFormat
from Models.Map.Position import Position
import xml.etree.ElementTree as xml
class ComunicationPorts:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__type=root.attrib['type']
        self.__name=root.attrib['name']
        self.__position=Position(float(root.attrib['x']),float(root.attrib['y']))
    def __str__(self):
        return (f'Port name: {self.__name} transport people by {self.__type}, placd in {self.__position.__str__()}')
