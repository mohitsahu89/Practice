class Employee:
    def __init__(self, name, dept):
        self._name = name
        self._dept = dept

    def __str__(self):
        return f"{self._name} is from {self._dept} department"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def dept(self):
        return self._dept

    @dept.setter
    def dept(self, dept: str):
        if not isinstance(dept, str):
            raise ValueError("Invalid datatype for department")
        self._dept = dept

emp1 = Employee("Mohit", "IT")
emp2 = Employee("Amit", "HR")

print(emp1)
print(emp2)

