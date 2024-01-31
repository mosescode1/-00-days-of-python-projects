travel_log = [
    {
        "country": "France",
        "Visits": 12,
        "cities": ["paris", "lille", "dijon"]    
    },
    {
        "country": "Germany",
        "Visits": 3,
        "cities": ["Berlin", "hamburg", "Sttugart"],
    },
]

def add(country, visits, cities):
    new_log = dict()
    
    new_log["country"] = country
    new_log["visits"] = visits
    new_log["cities"] = cities
    travel_log.append(new_log)
    

add("Russia", 3, ["Moscow", "st petersburg"])

print(travel_log)