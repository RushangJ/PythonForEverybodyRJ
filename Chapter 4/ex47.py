#Exercise 7: Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.

#old code:
#score= input("Enter score:")
#try:
#    float(score)
#    if float(score)>1.0:
#        print('Bad Score')
#    elif float(score)>=0.9:
#        print('A')
#    elif float(score)>=0.8:
#        print('B')
#    elif float(score)>=0.7:
#        print('c')
#    elif float(score)>=0.6:
#        print('D')
#    elif float(score)<0.6:
#        print('F')
#except:
#    print('Bad Score')

score= input("Enter score: ")

def computegrade(score):
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
print(computegrade(score))
