
# a class for DFAs
# modify as needed
class DFA :

    # init the DFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # transition function
        self.q0 = q0 # initial state
        self.F = F # final states
   
   # print the data of the DFA
    def __repr__(self) :
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the DFA on the word w
    # return if the word is accepted or not
    # modify as needed
    def run(self, w) :
        # run always starts at q0 starting state
        current_state = self.q0
        for symbol in w:
            if symbol not in self.Sigma:
                print(f"Error: Symbol '{symbol}' not in the alphabet {self.Sigma}.")
                return False
    
            current_state = self.delta.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.F
    
    def refuse(self) :
        new_F = []
        for state in self.Q :
            if state not in self.F :
                new_F.append(state)
        return DFA(self.Q, self.Sigma, self.delta, self.q0, set(new_F))

