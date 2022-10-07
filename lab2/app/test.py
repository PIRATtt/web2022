number='79787250588' #11
number=number.strip('()+-. ')
if 9<len(number)<12 and number.isdigit()==True:
    if len(number)==10:
        number='+7'+number
    elif len(number)==11:
        pass
else:
    print('ERROR!')