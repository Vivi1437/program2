mylist=input("Enter a list of numbers seperated by spaces:")
mylist=list(map(int,mylist.split()))
sum=0
for num in mylist:
    sum+=num
    print("The sum of the numbers is:",sum)
