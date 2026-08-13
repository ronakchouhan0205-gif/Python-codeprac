def classify_number(num):
    match num:
        case n if n<0:
            return "Negative"
        case n if n==0:
            return "Zero"
        case n if n>=1 and n<=10:
            return "Small positive"
        case n if n>10:
            return "Large positive"
        case _:
            return "Invalid value"
print(classify_number(21))
