
class Animal(object):
    '''动物的基础类'''
    #设置标签为动物
    tag = '动物'
    #定义一个方法为eat，动物都要吃东西
    def eat(self):
        print('动物都需要吃东西')

class Cat(Animal):
    '''猫科动物，继承父类Animal'''
    #标签为麦科动物
    tag = '猫科动物'
    #定义猫的构造方法
    def __int__(self,name,age):
        self.name = name    #猫都有名称
        self.age = age    #猫都有年龄
        print(f'我叫{self.name}，我今年{self.age}岁')


    #定义猫的eat方法，继承父类的需要吃东西，然后还喜欢吃鱼
    def eat(self):
        super().eat()
        print('猫还喜欢吃小黄鱼')

    #定义一个catch方法，猫还会捉老鼠
    def catch(self):
        print('猫还会捉老鼠')

class OrangeCat(Cat):
    '''中国田园猫'''
    #添加一个标签，中华田园猫
    tag = '中华田园橘猫'
    #定义一个方法，猫会叫
    def cry(self):
        print('橘猫还会喵喵叫')

    def eat(self):
        super().eat()
        print('我还喜欢吃老鼠')

if __name__=='__main__':
    #实例化Cat类
    cat=Cat()
    cat.__int__('小黄',3)
    #实例化橘猫
    oragecat=OrangeCat()
    #调用吃的方法，继承了animal类，所以会打印'动物都需要吃东西',
    # 继承了Cat类，所以会打印'猫都喜欢吃小黄鱼'，还有自己的eat方法'喜欢吃老鼠'
    oragecat.eat()
    #调用猫的cry方法
    oragecat.cry()
    #调用父类的捉老鼠方法，猫还会捉老鼠
    oragecat.catch()

