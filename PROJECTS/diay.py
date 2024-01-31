# calcuate the number of days, weeks, monnth left until 90
age = int(input("Enter your age"))
age_left = 90 - age
month = 12 * age_left
days = 365 * age_left
weeks = 52 * age_left
print(month, days, weeks)