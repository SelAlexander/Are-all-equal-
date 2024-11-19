first = int(input())
second = int(input())
third = int(input())
print(first, second, third)
if first == second and second == third and first == third :
    print(3)
elif first == third or second == first or third == second  :
    print(2)
else:
    print(0)
