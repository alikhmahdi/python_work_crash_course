print(f"Is the 'mahdi' equal to 'mahdi'? {'mahdi' == 'mahdi'}")
print(f"Is the 'mahdi' unequal to 'mahdi'? {'mahdi' != 'mahdi'}")
print(f"Is the 'mohammad' equal to 'mahdi'? {'mohammad' == 'mahdi'}")
print(f"Is the 'mohammad' unequal to 'mahdi'? {'mohammad' != 'mahdi'}")


print(f"Is the 'mahdi' equal to 'Mahdi'(case matters)? {'mahdi' == 'Mahdi'}")
print(f"Is the 'mahdi' equal to 'Mahdi'(case doesn't matter)? {'mahdi' == 'Mahdi'.lower()}")


print(f'Is the 5 equal to 10? {5 == 10}\n')
print(f'Is the 5 unequal to 10? {5 != 10}\n')
print(f'Is the 5 equal to 5? {5 == 5}\n')
print(f'Is the 5 unequal to 5? {5 != 5}\n')
print(f'Is the 5 greater than 10? {5 > 10}\n')
print(f'Is the 5 greater than or equal to 10? {5 >= 10}\n')
print(f'Is the 5 greater than 10? {5 > 4}\n')
print(f'Is the 5 greater than or equal to 10? {5 >= 4}\n')
print(f'Is the 5 less than 10? {5 < 10}\n')
print(f'Is the 5 less than or equal to 10? {5 <= 10}\n')
print(f'Is the 5 less than 10? {5 < 4}\n')
print(f'Is the 5 less than or equal to 10? {5 <= 4}\n')


print(f'Is the 5 less than 10 and bigger than 0? {5 < 10 and 5 > 0}\n')
print(f'Is the 5 less than 4 and bigger than 0? {5 < 4 and 5 > 0}\n')
print(f'Is the 5 less than 10 and bigger than 6? {5 < 10 and 5 > 6}\n')
print(f'Is the 5 less than 4 and bigger than 6? {5 < 4 and 5 > 6}\n')
print(f'Is the 5 less than 10 or bigger than 0? {5 < 10 or 5 > 0}\n')
print(f'Is the 5 less than 4 or bigger than 0? {5 < 4 or 5 > 0}\n')
print(f'Is the 5 less than 10 or bigger than 6? {5 < 10 or 5 > 6}\n')
print(f'Is the 5 less than 4 or bigger than 6? {5 < 4 or 5 > 6}\n')


numbers = list(range(10, 100, 10))
print(f'Numbers: {numbers}\n')
print(f'Is the 50 involves in the numbers? {50 in numbers}\n')
print(f'Is the 25 involves in the numbers? {25 in numbers}\n')
print(f'Is the 50 doesn\'t involve in the numbers? {50 not in numbers}\n')
print(f'Is the 25 doesn\'t involve in the numbers? {25 not in numbers}\n')