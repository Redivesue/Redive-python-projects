# Practice 89
def intConvertSeq(n):
    if n<0 or n>12:
        seq = " "
        return seq
    else:
        if n == 1:
            seq = "First"
            return seq
        elif n == 2:
            seq = "Second"
            return seq
        elif n == 3:
            seq = "Third"
            return seq
        elif n ==4:
            seq = "Fourth"
            return seq
        elif n ==5:
            seq = "Fifth"
            return seq
        elif n ==6:
            seq = "Sixth"
            return seq
        elif n ==7:
            seq = "Seventh"
            return seq
        elif n ==8:
            seq = "Eighth"
            return seq
        elif n ==9:
            seq = "Ninth"
            return seq
        elif n ==10:
            seq = "Tenth"
            return seq
        elif n ==11:
            seq = "Eleventh"
            return seq
        elif n ==12:
            seq = "Twelfth"
            return seq

def main():
    n = int(float(input("Enter a number: ")))
    return n

if __name__ == '__main__':
    print(intConvertSeq(main()))



