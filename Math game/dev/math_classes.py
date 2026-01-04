import random

class MathOperations: ## Arithmatic functions
    def multiplacation(x1,x2): # Multiplication
        value = int(x1*x2)
        return value
    def divission(X,random_x1,random_x2): # Divission
        isFloat = True
        while isFloat:
            value = random.randint(random_x1,random_x2)            
            if X % value == 0:
                return value
    def addition(x1,x2): # Addition
        value = int(x1+x2)
        return value
    def subtraction(x1,x2): # Subtraction
        value = int(x1-x2)
        return value
    

    ##def ScoreCheck(modes,difficulty,rounds,dict,score): ## !! UNFINISHED NO UNCOMMENT

#ScoreData.Encrypt() ##  UNCOMMENT TO TEST
#ScoreData.Decrypt(modes="a",difficulty="impossible",points=10) ##  UNCOMMENT TO TEST