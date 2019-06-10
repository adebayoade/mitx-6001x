varA = 'girl'
varB = 5
if type(varA) == str or type(varB) == str:
    print("string involved")
elif len(varA) > len(varB):
    print("bigger")
elif varA == varB:
    print("equal")
elif len(varA) < len(varB):
    print("smaller")
