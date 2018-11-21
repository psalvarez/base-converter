def translate(digit):
    uni_offset = 64
    return str(chr(uni_offset + digit))


def addDigit(nu_digit, chain): #adds the digit to the output
    trans_digit = translate(nu_digit) #translates from the original system to the new one
    return trans_digit + chain


base = 27
out = ""

rem = 0 #remainder of each division
res = int(input("Enter the number to convert: ")) #result of each division

#Main loop
while (res != 0):
    #Modulo
    rem = res%base
    #Divide (using integer division)
    res = res//base
    #Add remainder to the output number
    out = addDigit(rem, out)

print("Excel column index: " + out)
