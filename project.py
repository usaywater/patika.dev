from tkinter import Y

yedekliste = []

def flat(l):
    for i in l:
        if type(i)==list:
            flat(i)

        else:
            yedekliste.append(i)

flat([["sude",["mükemmel"],[[[["birisi"]]]]],2022,["patika.dev"]])

print(yedekliste)


x = [[1, 2], [3, 4], [5, 6, 7]]
yedek = []

def terscevir(l):
    for i in l:
        if type(i)==list:
            yedek.append(list(reversed(i)))
            
            
    
terscevir([[1, 2], [3, 4], [5, 6, 7]])
print(list(reversed(yedek)))