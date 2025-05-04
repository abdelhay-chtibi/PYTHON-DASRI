if (5 > 7) :
    print("True")
else:
    print("False")

print("----------------------------------------------------")

jour = 5 > 7
if jour : 
    print("Bonjour")
else:
    print("Bonsoir")

print("----------------------------------------------------")

x = 10
if x > 10 :
    print(x, "est plus grand que 10")
elif x < 10:
    print(x, "est plus petite que 10")
elif x == 10 :
    print(x, "est egal que 10") 
    
print("----------------------------------------------------")

x = 6
# les conditions
condition1 = x>0; condition2 = x<9; condition3= x==2; condition4 = x == 3; 
condition5 = (x==5) or (x==7); condition6 = x<0; condition7= x>9

if condition1 and condition2:  ## remarquer qu'on a pas besoin de faire condition1==True
    if condition3 or condition4 or condition5:
        print(x, "est premier")
    else:
        print(x, "n'est pas premier")
else:
    if condition6:
        print(x, "est négatif")
    else:
        print(x, "est supérieur à 9")