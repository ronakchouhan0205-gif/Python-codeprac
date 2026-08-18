def day_name(num):
    match num:
        case n if n == 1:
            return "Monday"
        case n if n == 2:
            return "Tuesday"
        case n if n == 3:
            return "Wednesday"
        case n if n == 4:
            return "Thursday"
        case n if n == 5:
            return "Friday"
        case n if n == 6:
            return "Satuday"
        case n if n == 7:
            return "Sunday"
        case _:
            return "Invalid day"
print(day_name(2))
