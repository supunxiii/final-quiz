largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        int_num = int(num)
        if largest is None:
            largest = int_num
        elif int_num > largest:
            largest = int_num
        elif smallest is None:
            smallest = int_num
        elif int_num < smallest:
            smallest = int_num
    except:
        print("Invalid input")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)
