dream_vacation = {
}
while True:
    if input(f"Is there anyone here want to talk about traveling ? (yes/no) ").lower() == 'no':
        break
    name = input("Hello my friend, What is your name? ")
    dream_vacation[name] = {
    }
    location = input("If you must have only one trip where would it be? ")
    dream_vacation[name]['location'] = location
    why = input(f"Why do you want to go to {location}? ")
    dream_vacation[name]['why'] = why
    who = input(f"Who will you be traveling with to {location}? ")
    dream_vacation[name]['who'] = who
    print(f'Thanks for your time, {name.title()}!')
print(f"Here's the information we gathered:")
for name, dictionery in dream_vacation.items():
    print(f"\n\n{name.title()}'s Information:")
    for key, value in dictionery.items():
        print(f" - {key.title()}: {value}")