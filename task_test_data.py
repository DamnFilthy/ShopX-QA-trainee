import pytest


def discount_machine(price: int, points: int):
    try:
        if 0 < points <= 100:
            discount = price * 0.01
        elif 100 < points <= 200:
            discount = price * 0.03
        elif 200 < points <= 500:
            discount = price * 0.05
        elif points > 500:
            discount = price * 0.1
        else:
            return 'Отрицательное значение.'
    except TypeError:
        return 'Неправильное значение.'

    total_price = price - discount

    return total_price


class TestSomething:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    @pytest.mark.parametrize('price, points, result', [
        (100, 99, 99), (2500, 124, 2425), (1800, 220, 1710),
        (1300, 345, 1235), (7600, 450, 7220), (6200, 550, 5580),
        (999, -215, 'Отрицательное значение.'), (8800, 'asd', 'Неправильное значение.')
    ])
    def test_discount_machine(self, price, points, result):
        assert discount_machine(price, points) == result

    def teardown_class(self):
        print('method teardown_class')
