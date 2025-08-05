def calculator():
    print("🧮 Simple Calculator")
    print("Operations: +  -  *  /")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation: ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("❌ Cannot divide by zero")
                return
        else:
            print("❌ Invalid operation")
            return

        print(f"✅ Result: {result}")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
