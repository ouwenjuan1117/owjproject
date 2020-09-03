from time import sleep
import pytest


@pytest.mark.run(order=3)
def test_mul():
    sleep(0.5)
    assert True


@pytest.mark.run(order=2)
def test_sub():
    sleep(0.5)
    assert True


@pytest.mark.last
def test_div():
    sleep(0.5)
    assert True


@pytest.mark.run(order=1)
def test_add():
    sleep(0.5)
    assert True
