import random

class CreateQuestions():

    factors = 1,10,100,1000
    
    
    
    def GenerateOperands(factor, fractional, quantity):
        """generates a list of operands given the number of digets and amount of qustions."""

        operands = []

        for i in range(1, quantity + 1):
            operand = random.randint(0,factor)
            operands.append(operand)

        if fractional == True:
            for i in range(0, quantity):
                operands[i] = operands[i] / random.choice(CreateQuestions.factors)

        
        return operands
    
    
    
        