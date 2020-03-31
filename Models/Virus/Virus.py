from Exceptions.BadArgumentFormat import BadArgumentFormat
import xml.etree.ElementTree as xml
from Models.Virus.HostInfluance import HostInfluence
from Models.Virus.Plague import Plague
class Virus:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__data=root.attrib['data']
        self.__place=root.attrib['place']
        self.__hostInfluance=[]
        self.__plague=[]
        self.__stat={}
        for i in root.iter('host'):
            self.__hostInfluance.append(HostInfluence(i))
        for i in root.iter('plague'):
            self.__plague.append(Plague(i))
        for i in root.iter('stat'):
            self.__stat[i.attrib['name']]=int(i.text)
    def __str__(self):
        output=""
        output+=f"Virus {self.__name} starts in {self.__place} on {self.__data}"
        for i in self.__hostInfluance:
            output+=f"\n{i.__str__()}"
        for i in self.__plague:
            output+=f"\n{i.__str__()}"
        for i in self.__stat.keys():
            output += f"\n{i}: {self.__stat[i]}"
        return output
