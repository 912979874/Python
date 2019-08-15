#定义一个函数
def test(num):
    def test_in(num_in):
        print("in test_in 函数，num_in is %d"%num_in)
        return num+num_in
    return test_in
#注意这⾥的10其实给参数num
ret = test(10)
#注意这⾥的200其实给参数num_in
print(ret(100))
print(ret(200))
print("---线性函数---")
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line
line1=line_conf(1,1)
line2=line_conf(4,5)
print(line1(5))
print(line2(5))
print()