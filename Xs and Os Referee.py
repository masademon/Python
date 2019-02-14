def checkio(result):
	rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'


import numpy as np

def checkio(list):
    L = []
    for x in range(0,len(list)):
        i = list[x]
        for l in i:
            L.append(l)
            
    L = np.array(L).reshape(3,3)
    
    if L[0][0] == L[0][1] == L[0][2] !=".":
        return L[0][0]
    elif L[0][0] == L[1][0] == L[2][0] !=".":
        return L[0][0]
    elif L[0][0] == L[1][1] == L[2][2] !=".":
        return L[0][0]
    elif L[0][2] == L[1][1] == L[2][0] !=".":
        return L[0][2]
    elif L[0][1] == L[1][1] == L[2][1] !=".":
        return L[0][1]
    elif L[0][2] == L[1][2] == L[2][2] !=".":
        return L[0][2]
    elif L[1][0]== L[1][1]== L[1][2] !=".":
        return L[1][0]
    elif L[2][0]==L[2][1]==L[2][2]!=".":
        return L[2][0]

    else:
        return 'D'


	


