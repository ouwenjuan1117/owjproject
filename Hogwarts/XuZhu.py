
'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
'''

# 从Hogwarts文件夹下导入Tonglao模块
from Hogwarts.TongLao import TongLao

class XuZhu(TongLao):
    # 虚竹不爱打架，只爱念经,定义一个read方法
    def read(self):
        print('不要打架，罪过罪过')

    #虽然虚竹不爱打击，但是是天山童姥的徒弟，所以也会天山折梅手
    def fight_zms(self,enemy_hp,enemy_power):
        #调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
        super().fight_zms(self.hp,self.power)
        print(f'我不喜欢打架，但是我也会天山折梅手，我的血量是{self.hp}，我的武力值是{self.power}')


if __name__ == '__main__':
    # 实例化虚竹这个类
    xuzhu = XuZhu(100,500)
    # 调用虚竹念经read的方法
    xuzhu.read()
    # #调用虚竹fight_zms的方法
    xuzhu.fight_zms(40,600)
