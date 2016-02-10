__author__ = 'Matthew OBrien'
import json


class DFA:
        states = None
        alphabet = None
        detail = None
        start = None
        accepting = None
        transitions = None

        # Constructor from the file name
        def __init__(self, file):
            dfa = json.load(open(file))
            self.detail = dfa["detail"]
            self.alphabet = dfa["alphabet"]
            self.states = dfa["states"]
            self.start = dfa["start"]
            self.accepting_state = dfa["accepting"]
            self.transitions = dfa["transitions"]


        # Builds the actual DFA using the construction above
        def build_dfa(self):
            return self

        # Displays the details of the DFA. What strings it will accept
        def dfa_display(self):
            print(self.detail)
            print("The possible alphabet of the DFA: ")
            print(self.alphabet)

        # Tests the input of the string against the DFA.
        def test_dfa(self, inputs):
            current = self.start

            # Check for bad inputs in each piece of the input
            for char in inputs:
                if char not in self.alphabet:
                    print("Invalid input " + char + ".")
                    return

                # Moves to the next state
                next = self.transitions[current][char]
                current = next

            # If the final state is in the accepting state, accept the string.
            if(current in self.accepting_state):
                print("The string " + inputs + " is in the language of the DFA")

            else:
                # If final state is not in an accepting state, reject string.
                print("The string " + inputs + " is NOT in the language of the DFA")


if __name__ == '__main__':

    # Alter the file name here to test other DFAs. Three test DFAs have been provided
    dfa = DFA("testDFA.json").build_dfa()
    dfa.dfa_display()
    print("Typing exit for the string will quit the program")
    while True:
        string = input("What is the string?")
        if(string == "exit"):
            break
        dfa.test_dfa(string)


