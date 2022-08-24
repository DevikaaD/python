lst=[]
n=int(input("Enter the numbers:"))

for i in range(0,n):
    element=int(input())
    lst.append(element)

count_even=0
count_odd=0
for num in  lst:
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1

print("The no of even numbers are:",count_even)
print("The no of odd numbers are:",count_odd)