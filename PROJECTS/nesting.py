sample = {
    "france": "paris",
    "germany": "dublin", 
}
# nesting a list in list
sample2 = {
    "France": ["paris", "lille", "dijon"],
    "Germany": ["Berlin", "hamburg", "Sttugart"]
    }

# nesting a dic in dic
sample3 = {
        "France": {"city_visited": ["paris", "lille", "dijon"],"total_visited": 3 },
        "Germany": {"city_visited": ["Berlin", "hamburg", "Sttugart"], "total_visited": 3 },
    }
# a dictionary inside  a list
sample4 = [
        {
            "country": "France",
            "city_visited": ["paris", "lille", "dijon"],
            "total_visited": 3 
        },
        {
            "country": "Germany",
            "city_visited": ["Berlin", "hamburg", "Sttugart"],
            "total_visited": 3 
        },
]

for i in range(len(sample4)):
    for key in sample4["city_visited"]:
        print(key[0])