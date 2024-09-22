import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, y):
    return math.pow(x, y)

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Square root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural logarithm (ln(x))")
        print("4. Power (x^y)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the Scientific Calculator. Goodbye!")
            break
        
        try:
            if choice == '1':
                x = float(input("Enter x: "))
                result = square_root(x)
                print(f"√{x} = {result}")
            elif choice == '2':
                x = int(input("Enter x: "))
                result = factorial(x)
                print(f"{x}! = {result}")
            elif choice == '3':
                x = float(input("Enter x: "))
                result = natural_log(x)
                print(f"ln({x}) = {result}")
            elif choice == '4':
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
                result = power(x, y)
                print(f"{x}^{y} = {result}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()