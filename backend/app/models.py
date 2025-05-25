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

# SET UP CLASS FOR RESORT
class Resort:
    def __init__(self, name, epic, ikon, state, country, ski_acres, base_elevation, top_elevation, trails, avg_snowfall, avg_days_snow, season_length):
        self.name = name
        self.epic = epic
        self.ikon = ikon
        self.state = state
        self.country = country
        self.ski_acres = ski_acres
        self.base_elevation = base_elevation
        self.top_elevation = top_elevation
        self.trails = trails
        self.avg_snowfall = avg_snowfall
        self.avg_days_snow = avg_days_snow
        self.season_length = season_length
    def get_name(self):
        return self.name
    def get_epic(self):
        return self.epic
    def get_ikon(self):
        return self.ikon
    def get_state(self):
        return self.state
    def get_country(self):
        return self.country
    def get_ski_acres(self):
        return self.ski_acres
    def get_base_elevation(self):
        return self.base_elevation
    def get_top_elevation(self):
        return self.top_elevation
    def get_trails(self):
        return self.trails
    def get_avg_snowfall(self):
        return self.avg_snowfall
    def get_avg_days_snow(self):
        return self.avg_days_snow
    def get_season_length(self):
        return self.season_length
    # SETTERS
    def set_name(self, name):
        self.name = name
    def set_epic(self, epic):
        self.epic = epic
    def set_ikon(self, ikon):
        self.ikon = ikon
    def set_state(self, state):
        self.state = state
    def set_country(self, country):
        self.country = country
    def set_ski_acres(self, ski_acres):
        self.ski_acres = ski_acres
    def set_base_elevation(self, base_elevation):
        self.base_elevation = base_elevation
    def set_top_elevation(self, top_elevation):
        self.top_elevation = top_elevation
    def set_trails(self, trails):
        self.trails = trails
    def set_avg_snowfall(self, avg_snowfall):
        self.avg_snowfall = avg_snowfall
    def set_avg_days_snow(self, avg_days_snow):
        self.avg_days_snow = avg_days_snow
    def set_season_length(self, season_length):
        self.season_length = season_length

