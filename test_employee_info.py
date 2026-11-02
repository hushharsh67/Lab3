import pytest
import employee_info


def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(24, 33)
    names = [item["name"] for item in result]
    assert (names == ["John", "Jane", "Mike"])


def test_get_employees_by_age_range_none():
    result = employee_info.get_employees_by_age_range(50, 60)
    assert (result == [])


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert (result == pytest.approx(60166.6667, abs=0.001))


def test_get_employees_by_dept_marketing():
    result = employee_info.get_employees_by_dept("Marketing")
    names = [item["name"] for item in result]
    assert (names == ["Jane", "Mary"])


def test_get_employees_by_dept_engineering():
    result = employee_info.get_employees_by_dept("Engineering")
    names = [item["name"] for item in result]
    assert (names == ["Chloe", "Mike"])


def test_get_employees_by_dept_unknown():
    result = employee_info.get_employees_by_dept("HR")
    assert (result == [])