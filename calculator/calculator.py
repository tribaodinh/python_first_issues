
class calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    #allow to preplace first input with old value from previous calculations  
    old_value_have = False
    #value from previous calulation
    old_value = 0
    
    #starting function
    
    def starting():
        #while loop to repeat until user give valid numbers
        while(True):
            try:
                #ask for first input but if old_value_have is true then first input is equal to old_value
                if calculator.old_value_have == False:
                    first = int(input("what is the first number: "))
                else:
                    first = calculator.old_value
                second = int(input("what is the second number: "))
                break
            #catch value errors and not break program
            except ValueError:
                print("please enter valid input")

        #create constuctor
        T = calculator(first, second)      
        T.operations() 

 
    #must use calculator.addition(number1, number2) to use function in function in class
    #or put @staticmethod above function to use self
    def addition(number1, number2):
        return number1 + number2
 
    def subtraction(number1, number2):
        return number1 - number2
  
    def multiplication(number1, number2):
        return number1 * number2 
    
    def divide(number1, number2):
        return number1 / number2
    
    def exponent(number1, number2):
        return number1 ** number2
    
    def nth_root(number1, number2):
        return number1 ** (1/number2)
    
  
    def ending(result):  
        print(f"this is the result: {result}") 

        #while loop to ask if they want keep value or start anew or end it
        while (True):
            asking = input("Do want to keep the result and continue(type \"continue\") or state anew (type \"new\") or end it (type \"end\"): ")
            
            if asking == "continue":
                calculator.old_value = result
                calculator.old_value_have = True
                calculator.starting() 
            if asking == "new":
                calculator.old_value_have = False
                calculator.starting()   
            if asking == "end":
                #exit program
                exit()

            print("Please enter valid input")


    def operations(self):
        #while loop for when the user pick something that is not a valid operation
        while(True):
            symbol = input("which operation do you want(+, -, /, *, ^ (the second number will be the exopent) or r (nth root, the second number will be the root)): ")

            if symbol == "+":
                calculator.ending(calculator.addition(self.first_number, self.second_number))
            if symbol == "-":
                calculator.ending(calculator.subtraction(self.first_number, self.second_number))
            if symbol == "/":
                calculator.ending(calculator.divide(self.first_number, self.second_number))
            if symbol == "*":
                calculator.ending(calculator.multiplication(self.first_number, self.second_number))
            if symbol == "^":
                calculator.ending(calculator.exponent(self.first_number, self.second_number))


calculator.starting()
