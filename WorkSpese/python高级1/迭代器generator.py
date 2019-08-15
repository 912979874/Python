#!/usr/bin/env python
#coding=utf-8
#列表
L = [ x*2 for x in range(5)]
#生成器
G = (x*2 for x in range(5))
#print(next(G))
for x in G:
    print(x*2);