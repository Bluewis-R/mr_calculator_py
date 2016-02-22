chem_input = {    'H':[0],}                     #The amout of chemical dictionary

formula= input("Test input: \n")
fl = len(formula) +1
fn=0
while fn != fl:
    if formula[fn].islower() == True:    #checks if its an element with more than one letter
        element = formula[fn,fn+1]
        chem_input[element] =+ 1
        fn += 1
    elif formula[fn].isupper() == True:                                               #This is for single letter elements
        element = formula[fn]
        chem_input[element] =+ 1        #DOES'T WORK FOR 3 LETTER ELEMENTS
        fn += 1                                      #E.G. Uup -
    else:
        if  formula[fn-1].islower() == True:
            element = formula[fn-2,fn-1]
            chem_input[element] =+ int(formula[fn])
            fn += 1
        else:
        element = formula[fn-1]
        chem_input[element] =+ int(formula[fn])

print(formula)
print(chem_input)
