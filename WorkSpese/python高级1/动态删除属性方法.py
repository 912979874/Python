class Persion:
    def __init__(self):
        self.name="xiaoming"
        self.age=18
    def eat(self):
        print("eat food")

    def run(self):
        print("%s在跑步" % (self.name))
P=Persion();
#删除属性
#del P.age;
#删除方法
delattr(Persion,"eat");
#P.eat();
P.run();
print(P.name);
#print(P.age);