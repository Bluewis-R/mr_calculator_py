chem_table = {    'H':[0],}                    
formula= input("Test input: (\n")
fl = len(formula) +1
fn=0
while fn != fl:
    if formula[fn+1].islower() == True:
        element = formula[fn:fn+1]
        if formula[fn+2].isdigit() == True:
            sub = formula[fn+2]
            chem_table[element] =+ int(sub)
        else:
            chem_table[element] =+ 1
    elif formula[fn].isupper() == True:
        element = formula[fn]
        if formula[fn+1].isdigit() == True:
            sub = formula[fn+1]
            chem_table[element] =+ int(sub)
        else:
            chem_table[element] =+ 1
print("TESTING")
print(formula)
print(chem_table)
