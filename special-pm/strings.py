class Character:
    def isWhitespace(current):
        if len(current) != 1:
               print("Invalid char!")
               quit(65)
        if current == ' ':
            return True
        else :
            return False

    def isDigit(current):
        if len(current) != 1:
               print("Invalid char!")
               quit(65)
        if current.isdigit():
            return True
        else:
            return False

    def isLetter(current):
        if len(current) != 1:
               print("Invalid char!")
               quit(65)
        if current.isalpha():
            return True

    def isUpperCase(current):
        if len(current) != 1:
               print("Invalid char!")
               quit(65)
        if current.isupper():
            return True
        else:
            return False

    def isLowerCase(current):
        if len(current) != 1:
               print("Invalid char!")
               quit(65)
        if current.islower():
            return True
        else:
            return False

    def whitespace():
        return ' '

    def toLowerCase(current):
        if len(current) != 1:
               print("Invalid char!")
               quit(65)
        return current.lower()

    def toUpperCase(current):
        if len(current) != 1:
               print("Invalid char!")
               quit(65)
        return current.upper()

class String:
    def charAt(string, index):
        if type(index) is not int:
            print("Index must be integer!")
        return string[index]

    def length(string):
        return len(str(string))
    
    def indexOf(string, indx):
        return string.index(indx)

    def cut(string, start, end):
        return string[start:end]

    def swapCase(string):
        return string.swapcase()

    def title(string):
        return string.title()

    def trip(string, char):
        return string.strip(char)

    def equals(string, string2):
        if string == string2:
            return True
        else:
            return False

    def isUpperCase(current):
        if current.isupper():
            return True
        else:
            return False

    def isLowerCase(current):
        if current.islower():
            return True
        else:
            return False

    def toLowerCase(current):
        return current.lower()

    def toUpperCase(current):
        return current.upper()

    def contains(string, char):
        if string.find(char) == -1:
            return False
        else:
            return True
        

class StringBuilder:
    value = []
    def __init__(self):
        self.value = []
    

    def add(self, string):
        self.value.append(string)

    def delete(self, index):
        self.value.pop(index)

    def clear(self):
        self.value.clear()

    def deleteByRange(start, end):
        del self.value[start:end]

    def pop(self):
        self.value.pop(len(self.value) - 1)

    def length(self):
        return str(len(self.value))

    def lengthAsString(self):
        return "length - " + str(self.length())

    def toString(self):
        return ''.join(self.value)

class HexStrings:
    def toHex(number):
        return hex(number)

    def fromHex(string_hex):
        return int(string_hex, 16)

######HEX VALUES FUNCTIONS TEST######
##print(HexStrings.toHex(5))
##print(HexStrings.fromHex('0x5'))
######HEX VALUES FUNCTIONS TEST######

######STRING BUILDER TEST######
##buffer = StringBuilder()
##buffer.add("special")
##buffer.add(Character.whitespace())
##buffer.add("key")
##print(buffer.toString())
##buffer.pop()
##print(buffer.toString())
##buffer.clear()
##print(buffer.lengthAsString())
######STRING BUILDER TEST######

######STRING FUNCTIONS TEST########
##print(String.swapCase("hello!"))
##print(String.equals("special key", "special lang"))
##print(String.equals("special key", "special key"))
##print(String.contains("google.com", "."));
##print(String.length("552"))
##print(String.charAt("2 + 32", 0))
##print(String.title("special key"))
##print(String.trip("     SPECIAL KEY :<<<<<<<", ":< "))
######STRING FUNCTIONS TEST########

###CHARACTER FUNCTIONS TEST######
##print(Character.isDigit("4"))
##print(Character.isLetter("n"))
##print(Character.isLowerCase("S"))
##print(Character.isLowerCase("s"))
##print(Character.isUpperCase("S"))
##print(Character.isWhitespace("s"))
##print(Character.isWhitespace(" "))
##print(Character.toLowerCase("SPACIOUS"))
##print(Character.toUpperCase("PyThOn"))
##print(Character.whitespace(), "- whitespace")
###CHARACTER FUNCTIONS TEST######

