import pytest


# 创建一个登陆的fixture方法，yield关键字激活了fixture的teardown方法
# fixture 是pytest的一个外壳函数，可以模拟setup teardown 操作
# yield之前的操作相当于setup，yield之后的操作相当于teardown
# yield相当于return，如果想要return一些测试数据，可以放在yield后面返回到测试用例中
@pytest.fixture(autouse=True)
def login():
    print('登陆操作')
    print('获取token')
    username = 'tom'
    password = '123456'
    # return [username,password]   #相当于没有teardown操作
    yield [username, password]
    print('登出操作')


# 擦拭用例1  需要提前登陆数据库
# 在执行测试用例之前回执行传入的fixture方法
def test_case1(connectDB):
    print(f'login username and password :{login}')
    print('测试用例1')


# 擦拭用例2  不需要提前登陆数据库
def test_case2():
    print('测试用例2')


# 擦拭用例3  需要提前登陆数据库
def test_case3():
    print('测试用例3')


# 擦拭用例4  需要提前登陆数据库
def test_case4():
    print('测试用例4')
