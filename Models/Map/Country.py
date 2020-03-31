import xml.etree.ElementTree as xml
from Models.Map.HumanAtribute import *
from Models.Map.Land import *

class Country:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__position=Position(float(root.attrib['x']),float(root.attrib['y']))
        self.__stat = {}
        self.__humanAttribute=[]
        self.__lands=[]
        for i in root.iter('countryStat'):
            self.__stat[i] = int(i.text)
        for i in root.iter('humanAttribute'):
            self.__humanAttribute.append(HumanAttribute(i))
        for i in root.iter('land'):
            self.__lands.append(Land(i))
    def __str__(self):
        output=f"Country named {self.__name} on {self.__position.__str__()}"
        for i in self.__stat.keys():
            output += f"\n{i}: {self.__stat[i]}"
        for i in self.__humanAttribute:
            output+=f"\n{i.__str__()}"
        for i in self.__lands:
            output+=f"\n{i.__str__()}"
        return output

