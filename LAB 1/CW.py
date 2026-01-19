print("Doing Divison without using operator")

a = 18
b = 3

def Division(a,b):
    count = 0
    total = a
    while total >= b:
        total -= b      # Reduce a by b
        count += 1      # Counter to keep record of how many times reduced "a" by "b"
    return count        

result = Division(a = 18, b = 3)
print("Result: ", result)
