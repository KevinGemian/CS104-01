#CS104
#Kevin Gemian
#conditions.py
temp = 'xyz'
x = temp
while temp != 'end':
    temp = input ('Please enter the current temperature (type END to kill program): ')
    x = temp
    if temp == 'end':
        print ('End of Program')
        break
    x = int(temp)
    if x >= 110:
        print ("Stay inside")
    elif x >= 90:
        print('Wear Shorts!')
    elif x >= 70:
        print('Short sleeves are fine')
    elif x >= 50:
        print('Wear a jacket!')
    elif x >= 32:
        print('Wear a heavy coat!')
    elif x <= 31:
        print('Stay inside')
    else: x = str(temp)

