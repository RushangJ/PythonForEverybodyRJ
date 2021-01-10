#Rewrite your pay computation with time-and-a-half for overtime andcreate a
#function called computepay which takes two parameters (hours and rate)

#old code:
#hrs= input('Enter Hours:')
#try:
#    float(hrs)
#    rate= input('Enter Rate:')
#    if float(hrs)> 40:
#       extra_time= float(hrs)-40
#       extra_pay=float(extra_time)*10*0.5
#       pay=((float(hrs)*float(rate))+float(extra_pay))
#       print('pay :',pay)
#    else:
#       print('pay :',float(hrs)*float(rate))
#except:
#       print('Error, please enter a numeric value')


hrs= input("Enter Hours: ")
try:
    float(hrs)
    rate= input("Enter Rate: ")
    if float(hrs)>40:
        extra_time=float(hrs)-40
        def computepay(extra_time,rate):
            total=(float(extra_time)*float(rate)*1.5)+(40*float(rate))
            return total
        x=computepay(extra_time,rate)
        print("Pay: ",x)
    else:
        def computepay(hrs,rate):
            total= float(hrs)*float(rate)
            return total
        y=computepay(hrs,rate)
        print("Pay:  ",y)
except:
    print("Error, please enter a numeric value")
