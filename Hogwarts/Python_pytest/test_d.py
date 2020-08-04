import pytest
import requests
import yaml


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',yaml.safe_load(open('./data.yml')))
def test_answer(a,b):
    assert func(a) == b

def test_answer2():
    assert func(4) == 5

class TestDemo:
    def test_a(self):
        print('a')

    def test_b(self):
        print('b')
    def test_c(self):
        print('c')

if __name__=='__main__':
    pytest.main(['test_d.py::TestDemo','-v'])