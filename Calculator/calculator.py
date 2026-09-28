class Calculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return self.num1 / self.num2

    def power(self):
        return self.num1 ** self.num2


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Choose an operation: ")

calc = Calculator(num1, num2)

if choice == "1":
    print("Result:", calc.add())

elif choice == "2":
    print("Result:", calc.subtract())

elif choice == "3":
    print("Result:", calc.multiply())

elif choice == "4":
    print("Result:", calc.divide())

elif choice == "5":
    print("Result:", calc.power())

else:
    print("Invalid choice")


print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
print("Power")