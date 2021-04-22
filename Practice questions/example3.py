x = input()
if type(eval(x)) == str:
    print( "value is a string")
elif type(eval(x)) == float:
    print(x, "is a float")
elif type(eval(x)) == complex:
    print(x , "is a complex")
elif int(x) == 0:
    print("The value is 0.")
elif type(eval(x)) == int:
    print(x, "is a integer")


#here i'm getting error for String value