from PROJECTS.celebdata import comp_data
import random, os

current_score = 0


comp_a_value = 0
comp_b_value = 0
while True:
    
    comp_a = ""
    comp_b = ""
    
    print(f"Current Score {current_score}")
# creating two random choice
    for _ in range(1):
        choice_1 = random.choice(comp_data)
        choice_2 = random.choice(comp_data)
        
    if choice_2 == choice_1:
        choice_2 = random.choice(comp_data)

    for keys, values in choice_1.items():
        if isinstance(values, int) == True:
            continue
        comp_a +=  values + ", "

    for keys, values in choice_2.items():
        if isinstance(values, int) == True:
            continue
        comp_b +=  values + ", "
        
    for keys, values in choice_1.items():
        if isinstance(values, int) == True:
            comp_a_value = values
            
    for keys, values in choice_2.items():
        if isinstance(values, int) == True:
            comp_b_value = values
        
            
        
    print(f"compare A: {comp_a}")
    print(f"compare B: {comp_b}")


    answer = input("Please enter: A or B ").lower()

    if comp_a_value > comp_b_value:
        comp_answer = "a"
    else:
        comp_answer = "b"

    if answer == comp_answer:
        print("correct")
        current_score += 1
        os.system('clear')
    else:
        print("loose", "game ending")
        break
        