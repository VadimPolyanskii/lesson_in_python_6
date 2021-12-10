# Тестируем функцию

def res(a, b):
    r = a * b
    return r


res(10, 10)


def test_func_res():
    assert res(10, 10) == 100

