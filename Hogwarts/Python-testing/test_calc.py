import pytest
import yaml
import sys

sys.path.append('../..')
from Hogwarts.pythoncode.calc import Calclator

with open('.\datas\calc.yml', encoding='UTF-8') as f:
    # 获取加法的参数
    datas_aa = yaml.safe_load(f)
    add_datas = datas_aa['add']['add_datas']
    print(add_datas)
    # 获取加法测试用例的标题
    add_ids = datas_aa['add']['add_ids']
    print(add_ids)

    # 获取除法的参数
    div_datas = datas_aa['div']['div_datas']
    print(add_datas)
    # 获取除法测试用例的标题
    div_ids = datas_aa['div']['div_ids']
    print(div_ids)


class TestCalc():

    def setup_class(self):
        print('开始计算')
        # 实例化计算器
        self.calc = Calclator()

    def teardown_class(self):
        print('结束计算')

    def setup(self):
        print('测试用例开始')

    def teardown(self):
        print('测试用例结束')

    @pytest.mark.parametrize('a,b,expect', add_datas, ids=add_ids)
    def test_add(self, a, b, expect):
        try:
            # 调用它的加法的方法
            result = self.calc.add(a, b)
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(a, str):
                raise TypeError('计算不支持字符串相加')
            elif isinstance(b, str):
                raise TypeError('计算不支持字符串相加')
        else:
            assert expect == result

    @pytest.mark.parametrize('a,b,expect', div_datas, ids=div_ids)
    def test_div(self, a, b, expect):
        try:
            # 调用它的减法的方法
            result = self.calc.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(a, str):
                raise TypeError('计算不支持字符串相加')
            elif isinstance(b, str):
                raise TypeError('计算不支持字符串相加')
            elif a == 0:
                raise Exception('除数不能为0')
            elif b == 0:
                raise Exception('被除数不能为0')
        else:
            assert expect == result
