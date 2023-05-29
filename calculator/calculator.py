import math

class calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    #allow to preplace first input with old value from previous calulations 
    old_value_have = False
    #value from previous calulation
    old_value = 0
    
    #starting function
    @staticmethod
    def starting():
        #while to repeat until user give valid numbers
        while(True):

            try:
                if calculator.old_value_have == False:
                    first = int(input("what is the first number: "))
                else:
                    first = calculator.old_value
                second = int(input("what is the second number: "))
                #way to break from loop
                break
            #catch value errors and not break program
            except ValueError:
                print("please enter valid input")

        #create constuctor
        T = calculator(first, second)   
        #start operation function
        T.operations() 


    #add the 2 numbers
    #must use calculator.addition(number1, number2) to use function in function in class
    #or put @staticmethod above function to use self
    def addition(number1, number2):
        return number1 + number2

    #subtract the 2 numbers
    def subtraction(number1, number2):
        return number1 - number2

    #multiplication the 2 numbers
    def multiplication(number1, number2):
        return number1 * number2

    #divide the 2 numbers
    def divide(number1, number2):
        return number1 / number2
    
    #CREATE FUNCTION TO END operations()
    def ending(self, result):
        #print result
        print(f"this is the result: {result}") 

        #while loop to ask if they want keep value or start anew or end it
        while (True):
            asking = input("Do want to keep the result and continue(type \"continue\") or state anew (type \"new\") or end it (type \"end\"): ")
            
            #check if the input is "continue"
            if asking == "continue":
                calculator.old_value = result
                calculator.old_value_have = True
                calculator.starting()   
            #check if the input is "new"
            if asking == "new":
                calculator.old_value_have = False
                calculator.starting()   
            #check if the input is "end"
            if asking == "end":
                exit()

            print("Please enter valid symbol")


    def operations(self):
        #while loop for when the user pick somethung that is not a valid operation
        while(True):
            symbol = input("which operation do you want(+, -, /, or *): ")
            #entering "+" will start addition function 
            if symbol == "+":
                self.ending(calculator.addition(self.first_number, self.second_number))
            #entering "-" will start subtraction function 
            if symbol == "-":
                self.ending(calculator.subtraction(self.first_number, self.second_number))
            #entering "/" will start divide function 
            if symbol == "/":
                self.ending(calculator.divide(self.first_number, self.second_number))
            #entering "*" will start mutiplication function 
            if symbol == "*":
                self.ending(calculator.multiplication(self.first_number, self.second_number))


calculator.starting()
