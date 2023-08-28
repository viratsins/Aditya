class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary


def sort_employees(employees, attribute):
    return sorted(employees, key=lambda employee: getattr(employee, 'get_' + attribute)())


def main():
    employees = [
        Employee('161E90', 'Raman', 41, 56000),
        Employee('161F91', 'Himadri', 38, 67500),
        Employee('161F99', 'Jaya', 51, 82100),
        Employee('171E20', 'Tejas', 30, 55000),
        Employee('171G30', 'Ajay', 45, 44000)
    ]

    choice = input("Enter sorting parameter (id, name, age, salary): ")
    sorted_employees = sort_employees(employees, choice)
    for employee in sorted_employees:
        print(f"ID: {employee.get_id()}, Name: {employee.get_name()}, Age: {employee.get_age()}, Salary: {employee.get_salary()}")


if __name__ == "__main__":
    main()
