def day_name(num):
    match num:
        case n if n == 1:
            print("Monday")
        case n if n == 2:
            print("Tuesday")
        case n if n == 3:
            print("Wednesday")
        case n if n == 4:
            print("Thursday")
        case n if n == 5:
            print("Friday")
        case n if n == 6:
            print("Satuday")
        case n if n == 7:
            print("Sunday")
        case _:
            print("Invalid day")
print(day_name(4))
