#!/usr/bin/env python
#coding=utf-8
# def fib():
#     print("starting...")
#     while True:
#         a = yield 4
#         print("a:",a);
# f = fib()
# print(f.__next__())
# print("*"*20)
# print(f.__next__())

def fib2(time):
    n = 0
    a,b =0,1
    while n<time:
        yield b
        a,b = b,a+b
        n+=1
    return "done"
f2 = fib2(5)
while True:
    try:
        x = next(f2)
        print("value:%d"%x)
    except StopIteration as e:
        print("生成器返回值：%s"%e.value)
        break