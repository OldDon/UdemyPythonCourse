import sys, time

#clock = time.clock()
#print (clock)

# tqbf = the quick brown fox jumps over the lazy dog

originalInt = 10
newInt = 0


def loopAround(addTen):
     newInt = originalInt + addTen

loopAround(10)
print(newInt)
originalText = input("What is this text? ")
howLongText = len(originalText)
print(originalText, "is", howLongText, "characters long") 