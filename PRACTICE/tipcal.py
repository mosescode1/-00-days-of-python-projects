print("Welcome to the tip calculator!")
bill = float(input("What was the total bill $"))
tip = int(input("How much tip would you love to give? 10, 12, 15: "))
split_people = int(input("How many people are spliting the bill: "))

bill_with_tip = (tip / 100 * bill) + bill
bill_per_person = bill_with_tip / split_people
final_bill = round(bill_per_person, 2) 
print("Each person to pay {}$".format(final_bill))