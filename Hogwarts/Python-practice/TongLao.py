'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，see_people方法，需要传入一个name参数
，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
#定义一个天山童姥类
class TongLao(object):
    #定义一个构造方法，有血量和武力值两个属性
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    #定义一个see_people的方法,需要传入一个参数
    def see_people(self,name):
        #如果传入”WYZ”（无崖子），则打印，“师弟！！！！”
        if name == '无崖子':
            print('师弟！！！！')
        #如果传入“李秋水”，打印“呸，贱人”
        elif name == '李秋水':
            print('呸，贱人！！！')
        #如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif name =='丁春秋':
            print('叛徒，我杀了你！！！')

    #定义一个fight_zms的方法，天山折梅手,
    def fight_zms(self,enemy_hp,enemy_power):
        #调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
        self.hp = self.hp / 2
        self.power = self.power * 10
        # 一轮对打过后，天山童姥的的血量和敌人的血量
        tonglao_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - enemy_power
        if tonglao_final_hp > enemy_final_hp:
            print("天山童姥赢了")
        elif tonglao_final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            raise Exception("no peace, 不要平局，战斗到最后一刻")

if __name__=='__main__':
    #实例化天山童姥，需要传入hp,power两个参数
    tonglao=TongLao(100,400)
    #调用see_people的方法,需要传入一个参数name
    tonglao.see_people('无崖子')
    #调用fight_zms的方法，天山折梅手,需要传入敌人的两个参数enemy_hp,enemy_power
    tonglao.fight_zms(30,600)
