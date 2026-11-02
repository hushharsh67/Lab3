import pytest
import price_info


def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    assert result == pytest.approx(46.75)


def test_cost_of_fruits_apple():
    result = price_info.cost_of_fruits('apple', 10)
    assert result == pytest.approx(12.0)


def test_cost_of_fruits_watermelon():
    result = price_info.cost_of_fruits('watermelon', 2)
    assert result == pytest.approx(13.0)


def test_cost_of_fruits_unknown():
    result = price_info.cost_of_fruits('durian', 3)
    assert result == 0