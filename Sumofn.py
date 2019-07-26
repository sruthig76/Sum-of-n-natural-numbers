#Sum of n natural numbers
a=int(input("Enter the value of n"))
sum=0
for num in range(1,a+1,1):
   sum = sum + num
print("Sum of ",a,"numbers is=",sum)
