from numba.core.compiler_machinery import pass_timings


class Person:
    def __init__(self, name, epic, ikon, age, trip_length, ski_days, max_budget):
        self.name = name
        self.epic = epic
        self.ikon = ikon
        self.age = age
        self.trip_length = trip_length
        self.ski_days = ski_days
        self.max_budget = max_budget
    def get_name(self):
        return self.name
    def has_pass(self):
        if self.ikon or self.epic:
            return True
        return False
    def get_age(self):
        return self.age
    def get_ski_days(self):
        return self.ski_days
    def get_trip_length(self):
        return self.trip_length
    def get_max_budget(self):
        return self.max_budget

    # Setters
    def set_name(self, name):
        self.name = name
    def set_epic(self, epic):
        self.epic = epic
    def set_ikon(self, ikon):
        self.ikon = ikon
    def set_age(self, age):
        self.age = age
    def set_ski_days(self, ski_days):
        self.ski_days = ski_days
    def set_max_budget(self, max_budget):
        self.max_budget = max_budget
    def set_trip_length(self, trip_length):
        self.trip_length = trip_length

