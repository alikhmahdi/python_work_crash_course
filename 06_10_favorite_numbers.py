favorite_numbers={
    'mahdi':[10, 4, 7, 13],
    'sobhan':[6, 1],
    'homaion':[7, 4, 9],
    'pedri':[8],
    'kian':[]
}
for name, numbers in favorite_numbers.items():
    if len(numbers) == 0:
        print(f"There's no favorite number for {name.title()}.")
    elif len(numbers) == 1:
        print(f"{name.title()}'s favorite number is:")
    else:
        print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")