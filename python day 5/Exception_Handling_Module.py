try:
    num = float(input("\nEnter numerator: "))
    den = float(input("Enter denominator: "))
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid")

finally:
    print("Program Completed")

