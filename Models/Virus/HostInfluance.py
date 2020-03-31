import xml.etree.ElementTree as xml
from Exceptions.BadArgumentFormat import BadArgumentFormat
from Models.Virus.Atack import Atack
from Models.Virus.Plague import Plague

class HostInfluence:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__attack=[]
        self.__plague=[]
        for i in root.iter('attack'):
            self.__attack.append(Atack(i))
        for i in root.iter('plague'):
            self.__plague.append(Plague(i))
    def __str__(self):
        output=''
        output+=f'Host: {self.__name}'
        for i in self.__attack:
            output+="\n"+i.__str__()
        for i in self.__plague:
            output+="\n"+i.__str__()
        return output

