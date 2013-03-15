##Travis Wye
## CS-110-2
##This program takes input from the user, first name, last name, and a sequence of DNA
## it then passes that DNA string into a counting function. This function counts repeating
##CAG's and passes the final count into a prediction function which produces a quick "diagnosis" of
## how much the disease has possibly progressed or if even penatrated the pacients system. 



## this function simply gets input from the User, Gets first and last name as well as the DNA string.
## prints the users info upon completion of all inputs above the count funct output. returns dna which
## is then passed into the countCAG function.
def get_input():
    fname = raw_input ("Please Enter Pacients FIRST name:  ")
    lname = raw_input ("Please Enter Pacients LAST name:  ")
    dna = raw_input ("Please Enter Pacients DNA sequence:  ")
    print str('Name: ') + fname, lname
    print str('DNA sequence: ') + dna
    return dna

##This function counts the number of 'CAG' repeates in the dna string which is passed in from the get_input
##function, it is the only paramater for this function. the while loop starts at 0 and increments 'Start' and 'threedig'
##by 3 each time the conditionn is true, these variables set the string slice to count only 3 letters in the string each time through.
## The loop continues until the start variable count exceeds the length of the dna. When the if statement inside of the while is true,
##start and threedig increase by 3. numCAG increases by 1. When the if statement is false it 'breaks' out of the loop with the break
##statement, skiping the else when it is false. The function returns numCAG which is the number of 'CAG's that were counted in a
##row from the beginning to the first slice that wasnt 'CAG'.
def countCAG(dna):
    start = 0
    threedig = 3
    numCAG = 0
    while start < len(dna):
        if dna[start:threedig] == 'CAG':
            numCAG += 1
            start += 3
            threedig += 3
        else:
           break
        
    return numCAG


## This function passes in the numCAG that was returned in the count function. It takes the numCAG count and evaluates it
## within if and elif statements. Depending on how large the number the if or elif's will return a tuple with two strings
## saving it into the (diag,affect) global variables.
def prediction(numCAG):
       
    if numCAG < 27:
        return ('Normal','Unaffected') 
    elif numCAG >= 27 and numCAG <= 35:
        return ('Intermediate','Unaffected') 
    elif numCAG >= 36 and numCAG <= 41:
        return ('Reduced Penetrance','Somewhat Affected')
    elif numCAG > 41:
        return ('Full Penetrance','Affected')
    else:
        print 'Invalid Input'



##this is my main program. It takes the dna returned from the input function and saves it into global dna, then passes dna
## into countCAG which saves the numCAG count into CAG which is then passed into the prediction function. This function saves what ever
## is returned by the prediction function as a tuple (diag,affect). The final line prints the Diagnosis under what was printed in the input function.

##__Main__
dna=get_input()
CAG = countCAG(dna)
print str(CAG) + ' CAG repeats'
(diag,affect)=prediction(CAG)
print 'Diagnosis: '+ diag+', '+ affect



