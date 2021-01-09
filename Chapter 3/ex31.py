# Rewrite your pay computation to give  the employee 1.5 times the hourly rate
# for hours worked above 40 hours.

hrs= input('Enter Hours:')
rate= input('Enter Rate:')

if float(hrs)> 40:
    extra_time= float(hrs)-40
    extra_pay=float(extra_time)*10*0.5
    pay=((float(hrs)*float(rate))+float(extra_pay))
    print('pay :',pay)
else:
    print('pay :',float(hrs)*float(rate))
