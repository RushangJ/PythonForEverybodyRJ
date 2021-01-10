#Exercise 2: Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.



largest = None
smallest = None
keepgoing = True
while keepgoing:
  prompt1 = 'Enter a number \n'
  line = input (prompt1)
  try:
     line = int(line)
     if smallest is None or line < smallest:
      smallest = line
     if largest is None or line > largest:
      largest = line
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print ('Invalid input')
      continue
print ('Maximum is',largest)
print ('Minimum is',smallest)
