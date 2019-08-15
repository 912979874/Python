def test():
    print("---in func---")
#调用函数
test()
#引用函数
ret = test
print(id(ret))
print(id(test))