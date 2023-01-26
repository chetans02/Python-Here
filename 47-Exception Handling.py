

try:
    print("Resource Open")
    a = int(input("Enter a No"))
    b = int(input("Enter a No"))

    print(a/b)

except ZeroDivisionError as e:
    print("Hey you cant divide no by Zero ",e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong")

finally:
    print("Resource Closed")