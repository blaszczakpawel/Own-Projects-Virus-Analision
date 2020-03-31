from Exceptions.BadArgumentFormat import BadArgumentFormat
from Models.Map.Position import Position
import xml.etree.ElementTree as xml

class City:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__position=Position(float(root.attrib['x']),float(root.attrib['y']))
        self.__stat={}
        for i in root.iter('cityStat'):
            self.__stat[i]=int(i.text)
    def __str__(self):
        output=""
        output+=f"City named {self.__name}, {self.__position.__str__()}"
        for i in self.__stat.keys():
            output+=f"\n{i}: {self.__stat[i]}"
        return output