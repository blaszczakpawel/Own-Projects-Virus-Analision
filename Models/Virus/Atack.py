import xml.etree.ElementTree as xml
from Exceptions.BadArgumentFormat import BadArgumentFormat

class Atack:
    def __init__(self,root):
        if not isinstance(root,xml.Element):
            raise BadArgumentFormat("Zly format",type(root),"<class 'xml.etree.ElementTree.Element'>")
        self.__name=root.attrib['name']
        self.__annoyance=root.attrib['annoyance']
        self.__killPower=root.attrib['killPower']
        self.__ageAtack=[]
        for i in root.iter('age'):
            self.__ageAtack.append({'from':i.attrib['from'],'to':i.attrib['to'],'value':float(i.text)})
    def __str__(self):
        output=''
        output+=f"Attacks {self.__name}, with annoyance: {self.__annoyance} and kill power: {self.__killPower}"
        for i in self.__ageAtack:
            output+=f"\n{i['from']}-{i['to']} teases {i['value']}/1"
        return output