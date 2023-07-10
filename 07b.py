class find_negative(Exception):
    pass
try:
    name=input( " Enter your name  : ")
    age=int(input("Enter your age  : "))
    if age<0:
        raise find_negative
    marks=[]
    for i in range(0,6):
        mark=float(input("Enter marks scored : "))
        marks.append(mark)
    dict_={"NAME":name,"AGE":age,"MARKS":marks}
    print("DETAILS : \n",dict_)
except find_negative:
    print("AGE IS NEGATIVE")
