import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)

def isend(string, i):
    if len(string) <= i+1:
        res = True
    else:
        res = False
    return res

def finddigit(string, fn):
    if string[fn].isdigit() == True:
        res = True
    else:
        res = False
    return res

def findatom(string, fn):           # finds the 1 or two digit Element              
    if isend(string, fn) == True:
        result = string[fn]
    else:
        if string[fn+1].islower() == True:
            result = string[fn:fn+2]
        else:
            result = string[fn]
    if result.isdigit() == True:
        result = False
    return result

def findnum(string, fn):            # finds the number after the element
    excl = False
    num = 0
    result = 0
    i = fn + 1
    m = fn + 1
    if isend(string, i-1) == True:
        excl = True
    else:
        if finddigit(string, i) == False:
            excl = True
        else:
            i += 1
            if isend(string, i-1) == True:
                num = 1
            else:
                if finddigit(string, i) == False:
                    num = 1
                else:
                    i += 1
                    if isend(string, i-1) == True:
                        num = 2
                    else:
                        if finddigit(string, i) == False:
                            num = 2
                        else:
                            num = 3
    k = m + num
    if excl == True:
        result = 1
    else:
        result = string[m:k]
    return result

def elemt_con(formula):
    fn = 0
    excl = False
    chem_table = {}
    while fn < len(formula):        
        elemt = findatom(formula, fn)
        if findatom(formula, fn) == False:
            fn += 1
        else:
            if len(elemt) == 1:
                num = findnum(formula, fn)            
            else:
                num = findnum(formula, fn+1)
            chem_table[elemt] = num
            if excl == True or formula:
                fn += len(elemt)
            elif num == 1:
                fn = len(elemt)
            else:
                fn = fn + len(elemt) + len(str(num))
    return chem_table
    
def start():
    print("Please use normal chemical syntax to input Formulae")
    print("E.G. H20,  NaSO4, C6H12O6")
    formula = input("==> ")
    chem_table = elemt_con(formula)
    molecularMass_sum = {}
    end_value = 0
    for element in chem_table:
        no_atoms = int(chem_table[element])
        mr_value = data["elements"][element]["MolecularMass"]
        result = no_atoms * mr_value
        end_value += result
    print(end_value)



start()


                

        
#list_of_elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg," "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg","Bh", "Hs", "Mt", "Ds", "Rg",]





















