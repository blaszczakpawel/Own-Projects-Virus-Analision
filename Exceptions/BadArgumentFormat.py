class BadArgumentFormat(Exception):
    def __init__(self,massege,actualFormat,needFormat):
        self.__massege=str(massege)
        self.__actualFormat=str(actualFormat)
        self.__needFormat=str(needFormat)
    def __str__(self):
        return (self.__massege + "\n" + " We need type of " + self.__needFormat + ", but you are geaving " + self.__actualFormat)
