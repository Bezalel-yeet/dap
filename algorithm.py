#basic calculator simulator
# user can keep inputting integers until a stopping condition is met



def addition():
    output  = 0
    for i in range (len(int_array)):
        output += int_array[i]
        i+=1
    print(output)

def subtraction():
    output = int_array[0]
    for i in range(1, len(int_array)):
        output -= int_array[i]
    print(output)

def multiplication():
    output = 1
    for i in range(len(int_array)):
        output *= int_array[i]
    print(output)

def division():
    output = int_array[0]
    for i in range(1, len(int_array)):
        output /= int_array[i]
    print(output)









int_array = []

while True:
    inputs = int(input("Enter a number: "))
    if inputs == 999:
        break
    int_array.append(inputs)
    
operator = input("Enter operator: addition,subtraction,division or multiplication: ")

if operator == "addition":
    addition()

if operator == "division":
    division()

if operator == "subtraction":
    subtraction()

if operator =="multiplication":
    multiplication()
     

