#!/usr/bin/env python
#coding=utf-8
from collections.abc import Iterable

def gen():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1
f=gen();
# print(next(f))
# print(next(f))
# print(next(f))
print("*"*50)
print(f.__next__());
print(f.send("haha"));
print(f.__next__());
print(f.__next__());
print("*"*50)
print(isinstance("a",Iterable))
print(isinstance("1",Iterable))

