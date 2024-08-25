import unittest
from secret_santa import SecretSanta, Employee

class TestSecretSanta(unittest.TestCase):
    def setUp(self):
        self.employees = [
            Employee("Alice", "alice@acme.com"),
            Employee("Bob", "bob@acme.com"),
            Employee("Charlie", "charlie@acme.com"),
        ]
        self.previous_assignments = {
            "alice@acme.com": "bob@acme.com",
            "bob@acme.com": "charlie@acme.com",
            "charlie@acme.com": "alice@acme.com",
        }
        self.secret_santa = SecretSanta("employees.csv", "previous_assignments.csv")
        self.secret_santa.employees = self.employees
        self.secret_santa.previous_assignments = self.previous_assignments

    def test_valid_assignment(self):
        self.assertTrue(self.secret_santa._is_valid_assignment(self.employees[0], self.employees[2]))
        self.assertFalse(self.secret_santa._is_valid_assignment(self.employees[0], self.employees[1]))

    def test_assign_secret_santas(self):
        self.secret_santa.assign_secret_santas()
        assignments = {emp.email: emp.secret_child.email for emp in self.secret_santa.employees}
        self.assertEqual(len(assignments), 3)
        self.assertNotIn(assignments["alice@acme.com"], ["alice@acme.com", "bob@acme.com"])

if __name__ == "__main__":
    unittest.main()
