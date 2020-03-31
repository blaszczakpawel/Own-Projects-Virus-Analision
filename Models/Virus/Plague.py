from Exceptions.BadArgumentFormat import BadArgumentFormat
import xml.etree.ElementTree as xml
class Plague:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__road=root.attrib['road']
        self.__distance=root.attrib['distance']
        self.__chance=root.attrib['chance']
    def __str__(self):
        return f"Virus could infect by {self.__road} on {self.__distance}m with chance {self.__chance}"