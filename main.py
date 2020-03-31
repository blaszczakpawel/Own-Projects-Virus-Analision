from Models.Virus.Virus import Virus
from xml.etree.ElementTree import *
import sys
from Models.Map.Position import Position
from Models.Map.Land import *
from Models.Map.Continent import *

tree = parse('Resources/lands.xml')
root = tree.getroot()
for i in root.iter('continent'):
    a=Continent(i)
    print(a)

