import os
import pytest
import yaml
import sys

# 获取命令行的当前路径
# sys.path.append('../..')
# sys.path.extend(['C:\\Users\\ouwenjuan\\.ssh\\owjproject\\Hogwarts'])

# mypath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# sys.path.append(mypath)
def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


sys.path.append(get_root_dir())


from Hogwarts.pythoncode.calc import Calclator


def pytest_collection_modifyitems(items):
    '''
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :param items:
    :return:
    '''
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# def pytest_addoption(parser):
#     mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
#     mygroup.addoption("--env",  # 注册一个命令行选项
#                       default='test',  # 默认值
#                       dest='env',  # 存储的变量
#                       help='set your run env'  # 参数说明
#                       )
#
#     mygroup.addoption("--dev",  # 注册一个命令行选项
#                       default='st',  # 默认值
#                       dest='dev',  # 存储的变量
#                       help='set your param'  # 参数说明
#                       )
#
#
# @pytest.fixture(scope='session')
# def cmdoption(request):
#     return request.config.getoption("--env", default='test')


@pytest.fixture(scope='module')
def connectDB():
    print('连接数据库操作')
    yield
    print('断开数据库连接')


@pytest.fixture(scope='session')
def get_calc():
    print('获取计算器的实例')
    calc = Calclator()
    return calc


# 通过os.path.dirname能够获取文件（conftest.py）所在的目录
yamlfilepath = os.path.dirname(__file__) + "/datas/calc.yml"
with open(yamlfilepath, encoding='UTF-8') as f:
    # 获取加法的参数
    datas_aa = yaml.safe_load(f)
    add_datas = datas_aa['add']['add_datas']
    # 获取加法测试用例的标题
    add_ids = datas_aa['add']['add_ids']

    # 获取除法的参数
    div_datas = datas_aa['div']['div_datas']
    # 获取除法测试用例的标题
    div_ids = datas_aa['div']['div_ids']

    # 获取乘法成功用例的参数的参数
    mul_datas_success = datas_aa['mul']['mul_datas_success']
    # 获取乘法成功测试测试用例的标题
    mul_ids_success = datas_aa['mul']['mul_ids_success']

    # 获取乘法失败用例的参数的参数
    mul_datas_fail = datas_aa['mul']['mul_datas_fail']
    # 获取乘法失败测试测试用例的标题
    mul_ids_fail = datas_aa['mul']['mul_ids_fail']

    # 获取减法成功用例的参数的参数
    sub_datas_success = datas_aa['sub']['sub_datas_success']
    # print(sub_datas_success)
    # 获取减法成功测试测试用例的标题
    sub_ids_success = datas_aa['sub']['sub_ids_success']
    # print(sub_ids_success)

    # 获取减法失败用例的参数的参数
    sub_datas_fail = datas_aa['sub']['sub_datas_fail']
    # print(sub_datas_fail)
    # 获取减法失败测试测试用例的标题
    sub_ids_fail = datas_aa['sub']['sub_ids_fail']
    # print(sub_ids_fail)


# 想要在方法前打印开始计算，结束计算，可以用yield
@pytest.fixture(params=add_datas, ids=add_ids)
# 获得加法的数据
def get_datas_add(request):
    print('开始计算')
    datas = request.param
    print(f'加法的测试数据是：{datas}')
    yield datas
    print('结束计算')


@pytest.fixture(params=div_datas, ids=div_ids)
# 获得除法的数据
def get_datas_div(request):
    print('开始计算')
    datas = request.param
    print(f'除法的测试数据是：{datas}')
    yield datas
    print('结束计算')


@pytest.fixture(params=mul_datas_success, ids=mul_ids_success)
# 获得乘法成功用例的数据
def get_datas_mul_success(request):
    print('开始计算')
    datas = request.param
    print(f'乘法的测试数据是：{datas}')
    yield datas
    print('结束计算')


@pytest.fixture(params=mul_datas_fail, ids=mul_ids_fail)
# 获得乘法失败用例的数据
def get_datas_mul_fail(request):
    print('开始计算')
    datas = request.param
    print(f'乘法的测试数据是：{datas}')
    yield datas
    print('结束计算')


@pytest.fixture(params=sub_datas_success, ids=sub_ids_success)
# 获得乘法成功用例的数据
def get_datas_sub_success(request):
    print('开始计算')
    datas = request.param
    print(f'减法的测试数据是：{datas}')
    yield datas
    print('结束计算')


@pytest.fixture(params=sub_datas_fail, ids=sub_ids_fail)
# 获得乘法失败用例的数据
def get_datas_sub_fail(request):
    print('开始计算')
    datas = request.param
    print(f'减法的测试数据是：{datas}')
    yield datas
    print('结束计算')
