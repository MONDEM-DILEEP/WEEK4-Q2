r=int(input("enter a range of numbers : "))
odd=0
even=0
for i in range(r) : 
    if i%2 == 0 :
        even+=1
    else : 
        odd+=1
print("the number of even numbers in the entered range is : ",even)
print("the number of odd numbers in the entered range is : ",odd)



   