#Write a  program to prompt for a score  between 0.0 and  1.0. If score  is out
#of range, print  an error message. If the score is between 0.0 and  1.0, print
#a grade  using the  following  table:


score= input("Enter score:")
try:
    float(score)
    if float(score)>1.0:
        print('Bad Score')
    elif float(score)>=0.9:
        print('A')
    elif float(score)>=0.8:
        print('B')
    elif float(score)>=0.7:
        print('c')
    elif float(score)>=0.6:
        print('D')
    elif float(score)<0.6:
        print('F')
except:
    print('Bad Score')
