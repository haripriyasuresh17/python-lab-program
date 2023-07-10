string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

index1 = 0
index2 = 0

while index1 < len(string1) and index2 < len(string2):
    if string1[index1] == string2[index2]:
        index1 += 1
        index2 += 1
    else:
        index1 += 1

if index2 == len(string2):
    print("YES")
else:
    print("NO")
