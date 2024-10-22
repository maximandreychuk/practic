class Department:
    def __init__(self, name: str, number_of_employees: int = None, budget: int = 100):
        self.name = name
        self.number_of_employees = number_of_employees
        self.budget = budget
        self.employyes = []

    def earn_money(self):
        pass

    def spend_money(self):
        pass

    @classmethod
    def create_department(cls, name, number_of_employees):
        return cls(name, number_of_employees)

    def add_employee(self, employee):
        self.employyes.append(employee)
        self.number_of_employees += 1

class Employee:
    def __init__(self, name, physical_condition: int = 100, mental_condition: int = 100):
        self.name = name
        self.physical_condition = physical_condition
        self.mental_condition = mental_condition

    def work(self):
        pass

    def chill(self):
        self.physical_condition = 100
        self.mental_condition = 100

    @staticmethod
    def employee_info(employee):
        return f"Сотрудник {employee.name}, ментальное состояние - {employee.mental_condition}, физ состояние - {employee.physical_condition}"


class Designer(Employee):
    def work(self):
        self.physical_condition -= 10
        self.mental_condition -= 20

class FurnitureWorker(Employee):
    def work(self):
        self.physical_condition -= 30
        self.mental_condition -= 10

class CreativeDepartment(Department):
    _inner_budget = 2

    def earn_money(self):
        self.budget += 10
        self._inner_budget += 1

    def spend_money(self):
        self.budget -= 8

class FurnitureDepartment(Department):
    _inner_budget = 3

    def earn_money(self):
        self.budget += 15
        self._inner_budget += 1

    def spend_money(self):
        self.budget -= 12


fd = FurnitureDepartment("Furniture", 50, )
nd = Department.create_department("Classic", 50)
print(nd.budget)
de = Designer("John")
print(de.employee_info(de))
de.work()
de.work()
print(de.employee_info(de))
