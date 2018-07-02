# encoding = UTF-8

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''

    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast



try:
    text = input('Enter someting-->')
    if len(text)<3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('eof')
except ShortInputException as ex:
    print('aaaaaaa{0},bbbbbbb{1}'.format(ex.length,ex.atleast))
else:
    print('no except')
