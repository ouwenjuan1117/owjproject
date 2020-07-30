"""
多个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。打斗多个回合
谁的hp先为0，那么谁就输了
"""
#定义一个fight()方法
def fight():
    # 定义四个变量，存放你的和我的血量还有攻击力
    my_hp = 1100
    my_power = 100
    your_hp = 1000
    your_power = 100
    # 对打多轮，谁的血量先小于等于0，谁就输了
    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        if my_hp<=0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break
# 调用fight 函数
fight()
