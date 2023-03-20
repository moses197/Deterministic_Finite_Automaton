"""
Created on Mon Mar 20-2023
Author: Moses
Topic: Deterministic Finite Automaton aka DFA
"""

class DFA():
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transtion functions as a dictionary
        self.q0 = q0 # initial states
        self.F = F # set of final states


    def __repr__(self) -> str:
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    def run(self, w):
        q = self.q0
        while w != "":
            q = self.delta[(q, w[0])]
            w = w[1:]
        return q in self.F


"""
    line of code below can be run on the terminal just:
        1. python3/python (depending on your OS) on the terminal then
        2. type/copy "from dfa import DFA" then
        3. type/copy the below code (except the print() and the code therein) and play with it with the lists of examples below ---> read the below comment section 
"""
D0 = DFA({0,1,2}, {"a", "b"}, 
        {   (0,"a"): 0, (0,"b"): 1,
            (1,"a"): 2, (1,"b"): 1,
            (2,"a"): 2, (2,"b"): 2
        },
        0,
        {0,1})

print(D0.run("abb")) # examples below can be run here too if you which to keep it simple but i must say... u are fecking lazy!!!

"""
    example of the strings to run
        1. D0.run("aa") # which is a valid state-> this will return true
        2. D0.run("aabbb") # valid
        3. D0.run("ba") # invalid
        4. D0.run("") # valid -- empty set is also a string that.... long story msg at mosesmoradeke@gmail.com for more on this
        5. D0.run("aba") #invalid
"""