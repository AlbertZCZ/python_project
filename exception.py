
try:
    year = int(input('plz input'))

    print(year)
except ValueError as e:
    print('dddd',e)
finally:
    print('finally....')