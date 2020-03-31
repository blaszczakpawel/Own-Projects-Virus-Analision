import xml.etree.ElementTree as xml
from Models.Map.Country import *

class Continent:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__position=Position(float(root.attrib['x']),float(root.attrib['y']))
        self.__stat = {}
        self.__countries=[]
        for i in root.iter('continentStat'):
            self.__stat[i] = int(i.text)
        for i in root.iter('country'):
            self.__countries.append(Country(i))
    def __str__(self):
        output=f"Continent named {self.__name} on {self.__position.__str__()}"
        for i in self.__stat.keys():
            output += f"\n{i}: {self.__stat[i]}"
        for i in self.__countries:
            output+=f"\n{i.__str__()}"
        return output

