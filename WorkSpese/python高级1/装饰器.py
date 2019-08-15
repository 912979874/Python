#第一波
from time import ctime ,sleep
def w1(func):
    def yanzheng():
        print("正在验证")
        print("验证50%")
        print("验证车成功")
        func()
    return yanzheng
@w1
def f1():
    print("f1")
    return "nihao"
@w1
def f2():
    print("f2")
f1()
f2()

def makeBold(fn):
    def webb():
        return "<b>"+fn()+"</b>"
    return webb
def makeItalic(fn):
    def webb():
        return "<i>"+fn()+"</i>"
    return webb
@makeBold
def test1():
    return "helloword01"
@makeItalic
def test2():
    return "helloword02"
@makeItalic
@makeBold
def test3():
    return "helloword03"
print(test1())
print(test2())
print(test3())
