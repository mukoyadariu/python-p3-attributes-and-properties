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
    def __init__(self, name="john", job="Purchasing"):
        self._name = ""
        self._job = ""

        self.set_name(name)
        self.set_job(job)

    def get_name(self):
        return self._name

    def get_job(self):
        return self._job

    def set_name(self, name):
        if (type(name) is str) and ((len(name) >= 1) and (len(name) <= 25 )):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name,)
    job = property(get_job, set_job,)