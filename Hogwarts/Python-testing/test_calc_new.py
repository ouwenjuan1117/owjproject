import os
import sys
# 获取命令行的当前路径
import yaml

sys.path.append('../..')


# yamlfilepath = os.path.dirname(__file__) + "/datas/calc.yml"
# with open(yamlfilepath, encoding='UTF-8') as f:
#     # 获取加法的参数
#     datas_aa = yaml.safe_load(f)
#
#     # 获取乘法成功用例的参数的参数
#     mul_datas_success = datas_aa['mul']['mul_datas_success']
#     print(mul_datas_success)
#     # 获取乘法成功测试测试用例的标题
#     mul_ids_success = datas_aa['mul']['mul_ids_success']
#     print(mul_ids_success)
#
#     # 获取乘法失败用例的参数的参数
#     mul_datas_fail = datas_aa['mul']['mul_datas_fail']
#     print(mul_datas_fail)
#     # 获取乘法失败测试测试用例的标题
#     mul_ids_fail = datas_aa['mul']['mul_datas_fail']
#     print(mul_ids_fail)


class TestCalc():

    def test_add(self, get_calc, get_datas_add):
        try:
            # 调用它的加法的方法
            result = get_calc.add(get_datas_add[0], get_datas_add[1])
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(get_datas_add[0], str) or isinstance(get_datas_add[1], str):
                raise TypeError('计算器不支持字符串')
            else:
                print(get_datas_add[0])
                print(get_datas_add[1])
                print('请输入正确的数据类型')
        else:
            assert get_datas_add[2] == result

    def test_div(self, get_calc, get_datas_div):
        if get_datas_div[1] == 0:
            print('除数不能为0')
        try:
            # 调用它的除法的方法
            result = get_calc.div(get_datas_div[0], get_datas_div[1])
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(get_datas_div[0], str) or isinstance(get_datas_div[1], str):
                raise TypeError('计算器不支持字符串')
            else:
                print(get_datas_div[0])
                print(get_datas_div[1])
                print('请输入正确的数据类型')
        else:
            assert get_datas_div[2] == result

    # 乘法成功的测试用例
    def test_mul_success(self, get_calc, get_datas_mul_success):
        result = get_calc.mul(get_datas_mul_success[0], get_datas_mul_success[1])
        if isinstance(result, float):
            result = round(result, 2)
        else:
            assert get_datas_mul_success[2] == result

    # 乘法失败的测试用例
    def test_mul_fail(self, get_calc, get_datas_mul_fail):
        try:
            result = get_calc.mul(get_datas_mul_fail[0], get_datas_mul_fail[1])
        except:
            if isinstance(get_datas_mul_fail[0], str) or isinstance(get_datas_mul_fail[1], str):
                raise TypeError('计算器不支持字符串')
            else:
                print(get_datas_mul_fail[0])
                print(get_datas_mul_fail[1])
                print('请输入正确的数据类型')
        else:
            assert get_datas_mul_fail[2] == result

    # 减法成功的测试用例
    def test_sub_success(self, get_calc, get_datas_sub_success):
        result = get_calc.sub(get_datas_sub_success[0], get_datas_sub_success[1])
        if isinstance(result, float):
            result = round(result, 2)
        else:
            assert get_datas_sub_success[2] == result

    # 减法失败的测试用例
    def test_sub_fail(self, get_calc, get_datas_sub_fail):
        try:
            result = get_calc.sub(get_datas_sub_fail[0], get_datas_sub_fail[1])
        except:
            if isinstance(get_datas_sub_fail[0], str) or isinstance(get_datas_sub_fail[1], str):
                raise TypeError('计算器不支持字符串')
            else:
                print(get_datas_sub_fail[0])
                print(get_datas_sub_fail[1])
                print('请输入正确的数据类型')
        else:
            assert get_datas_sub_fail[2] == result
