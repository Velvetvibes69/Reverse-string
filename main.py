#Input a word or scentence
string= input("Please enter your own string: ")

string2= ('')
#loop for printing in reverse
for i in string :
    string2= i + string2

    print("\nThe original string= ", string)
    print("The reverse string= ", string2)