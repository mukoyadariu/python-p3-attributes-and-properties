#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John", job="Purchasing"):
        self._name = ""
        self._job = ""

        self.name = name  # Utilize the property setters
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")

# Example usage
person1 = Person("Alice", "Sales")
print(person1.name)  # Output: Alice
print(person1.job)   # Output: Sales

person2 = Person("Bob", "Engineering")  # This will print the job error message
