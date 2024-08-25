import csv
import random
from typing import List, Dict

class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.secret_child = None

class SecretSanta:
    def __init__(self, employees_file: str, previous_assignment_file: str):
        self.employees_file = employees_file
        self.previous_assignment_file = previous_assignment_file
        self.employees = self._load_employees()
        self.previous_assignments = self._load_previous_assignments()

    def _load_employees(self) -> List[Employee]:
        employees = []
        with open(self.employees_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
        return employees

    def _load_previous_assignments(self) -> Dict[str, str]:
        previous_assignments = {}
        with open(self.previous_assignment_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                previous_assignments[row['Employee_EmailID']] = row['Secret_Child_EmailID']
        return previous_assignments

    def _is_valid_assignment(self, giver: Employee, receiver: Employee) -> bool:
        # Check that the giver is not the receiver and hasn't been assigned the same receiver as last year
        if giver.email == receiver.email:
            return False
        if self.previous_assignments.get(giver.email) == receiver.email:
            return False
        return True

    def assign_secret_santas(self) -> None:
        unassigned = self.employees[:]
        for giver in self.employees:
            potential_receivers = [emp for emp in unassigned if self._is_valid_assignment(giver, emp)]
            if not potential_receivers:
                raise ValueError(f"Cannot assign a valid Secret Child to {giver.name}. Try shuffling the employees.")
            receiver = random.choice(potential_receivers)
            giver.secret_child = receiver
            unassigned.remove(receiver)

    def save_assignments(self, output_file: str) -> None:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'])
            for employee in self.employees:
                writer.writerow([employee.name, employee.email, employee.secret_child.name, employee.secret_child.email])

