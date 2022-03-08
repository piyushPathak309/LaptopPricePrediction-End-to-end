str=input("Enter String")

for i in range(len(str)):
    if str[i] in ('a','e','i','o','u') :
        print("String is acceptable becoz it contains vowel")
    else:
        print("String is not acceptable becoz it don't contains vowel")



