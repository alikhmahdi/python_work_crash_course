ages = [1, 3, 10, 15, 30, 80]
for age in ages:
    print(f'\n\nPerson\'s age: {age}')    
    if age < 2:
        print("The person is a baby.")
    elif age < 4:
        print("The person is a toddler.")
    elif age < 13:
        print("The person is a child.")
    elif age < 20:
        print("The person is a teenager.")
    elif age < 65:
        print("The person is an adult.")
    else:
        print("The person is an elder.")
