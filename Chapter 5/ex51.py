#Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.

sum=0
count=0
average=0

while True:
        x=input("Enter a number: ")
        if x=="done":
            break
        try:
            y=float(x)
        except:
            print("Invalid Input.")
            continue
        sum=y+sum
        count=count+1
        average=sum/count

print(sum,count,average)
