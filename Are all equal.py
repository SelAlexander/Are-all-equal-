first = 361
second = 50
third = 128
if first == second or second == third or first == third :
    print(first, second, third)
elif first != second and second == third and first != third :
    print(second, third)
elif first == second and second != third and first != third :
    print(first, second)
elif first != second and second != third and first == third :
    print(first, third)
else:
    print(0)
