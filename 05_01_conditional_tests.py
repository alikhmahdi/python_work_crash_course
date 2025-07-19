car = 'BMW'
print(f'Is the car a Benz? {car == "Benz"}\n')
print(f'Is the car a Toyota? {car == "Toyota"}\n')
print(f'Is the car a BMW? {car == "BMW"}\n')


num = 5
print(f'Is the number greater than 10? {num > 10}\n')
print(f'Is the number less than 10? {num < 10}\n')
print(f'Is the number equal to 5? {num == 5}\n')


num = 100
print(f'Is the number single digit? {num < 10 and num > 0}\n')
print(f'Is the number double digit? {num >= 10 and num < 100}\n')
print(f'Is the number third digit? {num >= 100 and num < 1000}\n')


locations = ['New York', 'Los Angeles', 'Chicago']
location = 'New York'
print(f'Is the location in the list of locations? {location in locations}\n')