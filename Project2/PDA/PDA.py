__author__ = 'Matt'
import json

class PDA:
    alphabet = None
    variables = None
    detail = None
    rules = None
    accepting = None
    test = ["!"]
    stack = None

    #Constructor from file
    def __init__(self, file):
        pda = json.load(open(file))
        self.alphabet = pda["alphabet"]
        self.detail = pda["details"]
        self.rules = pda["rules"]
        self.accepting = pda["accepting"]
        self.variables = pda["variables"]


    #Builds the PDA from the constructor
    def build_PDA(self):
        return self

    def pda_display(self):
        print(self.detail)
        print("The possible alphabet of the PDA:")
        print(self.alphabet)


    def test_pda(self, inputs):
        stackEnd = ["!", "S"]

        for char in inputs:
            #Check #1 for an empty list
            if stackEnd == []:
                print("BAD STRING!!")
                return
            #Half way marker of the string
            if char == "#":
                stackEnd.pop()

            if stackEnd == []:
                print("BAD STRING!!")
                return

            if stackEnd[-1] in self.variables and char in self.alphabet:
                stackTemp = self.rules[stackEnd[-1]][char]
                stackEnd.pop()
                stackEnd += stackTemp

            if stackEnd[-1] in self.alphabet and char == stackEnd[-1]:
                stackEnd.pop()

            #print("Test5", stackEnd)
            #print(stackEnd[-1])
            #print(char)

        #print(stackEnd)
        if stackEnd == self.accepting:
            print("Acceptable string!")
        else:
            print("BAD STRING!!")




if __name__ == '__main__':

    # Alter the file name here to test other PDAs.
    pda4 = PDA("rules4.json").build_PDA()
    pda4.pda_display()
    print("Typing exit for the string will quit the program")
    while True:
        string = input("What is the string?")
        if(string == "exit"):
            break
        pda4.test_pda(string)










































