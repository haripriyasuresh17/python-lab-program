a= set(input("Enter elements of the first set separated by comma: ").split(',')) 
b = set(input("Enter elements of the second set separated by comma: ").split(',')) 
c = True
for i in b:
    if i not in a:
        c = False
        break
if c:
    print("True")
else:
    print("False")
