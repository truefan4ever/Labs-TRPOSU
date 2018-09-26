promt = "Enter the letter:"
a = str(input(promt))
dict = {'101':'a',
        '102':'b',
        '103':'c',
        '104':'d',
        '105':'e',
        '201':'f',
        '202':'g',
        '203':'h',
        '204':'i',
        '205':'j'
        }

for key, value in dict.items():
    if a == value:
        if int(key) < 106:
            print("1")
        elif int(key) > 106 and int(key) < 206:
            print("2")