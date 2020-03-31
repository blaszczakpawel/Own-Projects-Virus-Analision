from Exceptions.BadArgumentFormat import BadArgumentFormat
import xml.etree.ElementTree as xml
class HumanAttribute:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__type = root.attrib['type']
        self.__power = float(root.attrib['power'])
        self.__frequency = float(root.attrib['frequency'])
    def __str__(self):
        return f"Human atribute of {self.__name} on {self.__type} with power of {self.__power} and {self.__frequency}/1 people"