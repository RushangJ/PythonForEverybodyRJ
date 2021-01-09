#Rewrite your pay  program using try and except so that  your program handle
#non-numeric input  gracefully by printing a message and exiting the program.


hrs= input('Enter Hours:')
try:
    float(hrs)
    rate= input('Enter Rate:')
    if float(hrs)> 40:
       extra_time= float(hrs)-40
       extra_pay=float(extra_time)*10*0.5
       pay=((float(hrs)*float(rate))+float(extra_pay))
       print('pay :',pay)
    else:
       print('pay :',float(hrs)*float(rate))
except:
       print('Error, please enter a numeric value')
