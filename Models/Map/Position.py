from Exceptions.BadArgumentFormat import BadArgumentFormat
class Position:
    def __init__(self,x,y):
        if (type(x)!=float):
            raise BadArgumentFormat("Zly format",type(x),"<class 'float'>")
        if (type(y)!=float):
            raise BadArgumentFormat("Zly format",type(y),"<class 'float'>")
        self.__x=x
        self.__y=y
    def __str__(self):
        return f'Position: (x,y)=({self.__x},{self.__y})'
