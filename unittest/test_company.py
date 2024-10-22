import unittest
from oop.company import Department, FurnitureDepartment, Designer
from unittest import mock


class TestDepartment(unittest.TestCase):
    def test_furniture_department(self):
        dep = FurnitureDepartment(name="assembly", number_of_employees=10, budget=20)
        self.assertEqual(dep.name, "assembly")
        self.assertEqual(dep.budget, 20)
        self.assertEqual(dep.number_of_employees, 10)

    def test_create_department(self):
        dep = Department.create_department("repair", number_of_employees=5)
        self.assertEqual(dep.name, "repair")
        self.assertEqual(dep.budget, 5)

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Designer("Bob")
        self.emp.work()

    def test_create_employee(self):
        assert self.assertEqual(self.emp.name, "Bob")

    def test_work_employee(self):
        assert self.assertEqual(self.emp.mental_condition, 80)
        assert self.assertEqual(self.emp.physical_condition, 90)

    def test_chill_worker(self):
        self.emp.chill()
        assert self.assertEqual(self.emp.mental_condition, 100)
        assert self.assertEqual(self.emp.physical_condition, 100)


if __name__ == '__main__':
    unittest.main()