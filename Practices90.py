# Practice 90
from Practices89 import intConvertSeq
def Lyric_From_One_To_Twelve(n):
    if n ==1:
        verses = "And a partridge in a pear tree."
    if n ==2:
        verses = "Two turtle doves,"
    if n ==3:
        verses = "Three French hens,"
    if n ==4:
        verses = "Four calling birds,"
    if n ==5:
        verses = "Five golden rings,"
    if n ==6:
        verses = "Six geese a-laying,"
    if n ==7:
        verses = "Seven swans a-swimming,"
    if n ==8:
        verses = "Eight maids a-milking,"
    if n ==9:
        verses = "Nine ladies dancing,"
    if n ==10:
        verses = "Ten lords a-leaping,"
    if n ==11:
        verses = "Eleven pipers piping,"
    if n ==12:
        verses = "Twelve drummers drumming,"
    return verses

def printPhaseOfLyrics(n):
    if n ==1:
        print("\nOn the " + intConvertSeq(1) + " day of Christmas, \nmy true love sent to me:")
        print("A partridge in a pear tree.")
    else:
        print("\nOn the " + intConvertSeq(n) + " day of Christmas, \nmy true love sent to me:")
        for i in range(n,0,-1):
            print(Lyric_From_One_To_Twelve(i))

def startFunction():
    for j in range(1,13):
        printPhaseOfLyrics(j)

if __name__ == '__main__':
    startFunction()
