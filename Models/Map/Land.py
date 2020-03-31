from Exceptions.BadArgumentFormat import BadArgumentFormat
from Models.Map.Position import Position
from Models.Map.ComunicationPorts import ComunicationPorts
from Models.Map.City import City
import xml.etree.ElementTree as xml

class Land:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__position=Position(float(root.attrib['x']),float(root.attrib['y']))
        self.__stat={}
        self.__communicationPorts=[]
        self.__citys=[]
        for i in root.iter('landStat'):
            self.__stat[i]=int(i.text)
        for i in root.iter('communicationPort'):
            self.__communicationPorts.append(ComunicationPorts(i))
        for i in root.iter('city'):
            self.__citys.append(City(i))
    def __str__(self):
        output=f"Land named {self.__name}, {self.__position.__str__()}"
        for i in self.__stat.keys():
            output+=f"\nstat: {i}: {self.__stat[i]}"
        for i in self.__citys:
            output+=f"\n{i.__str__()}"
        for i in self.__communicationPorts:
            output+=f"\n{i.__str__()}"
        return output