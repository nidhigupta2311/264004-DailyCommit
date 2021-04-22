print("Enter the number of pizza slices you want :")
no = int(input())
c = 123
if no%2 == 0:
    total = no * 120
else:
    total = no * 123
print("Total cost:", total)