import math
class Calculator:
    def evaluate_expression(self, expression):
        try:
            if '+' in expression:
                a, b = map(float, expression.split('+'))
                return self.add(a, b)
            elif '-' in expression:
                a, b = map(float, expression.split('-'))
                return self.subtract(a, b)
            elif '*' in expression:
                a, b = map(float, expression.split('*'))
                return self.multiply(a, b)
            elif '/' in expression:
                a, b = map(float, expression.split('/'))
                return self.divide(a, b)
            elif '^' in expression:
                a, b = map(float, expression.split('^'))
                return self.power(a, b)
            elif '#' in expression:
                a = float(expression.split('#')[1])
                return self.square_root(a)
            else:
                return "Error: Invalid operation"
        except ValueError:
            return "Error: Invalid input format"
        except Exception as e:
            return f"Error: {str(e)}"
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

    def power(self, base, exponent):
        result = 1
        for _ in range(abs(int(exponent))):
            result = self.multiply(result, base)
        return result if exponent >= 0 else 1 / result

    def square_root(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return "Error: Cannot calculate the square root of a negative number"

if __name__ == "__main__":
    calc = Calculator()
    while True:
        user_input = input("Enter an expression (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        result = calc.evaluate_expression(user_input)
        print(f"Result: {result}")
