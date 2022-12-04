
def celsuis_to_fah(celsuis):
    #"""
    #this is a function to coonvrt celsuis to fahrenheit temp.
    #:param celsuis: float
    #:return: float

    #>>>  celsuis_to_fah(16)
    #60.8
    #"""

    fah = celsuis* 1.8 + 32
    return fah

celsuis = float(input("Enter celsuis value:"))
print(celsuis_to_fah(celsuis))

