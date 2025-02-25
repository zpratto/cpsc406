import dfa

def __main__() :

    Q1 = {1, 2, 3, 4}
    Sigma1 = ['a', 'b']
    delta1 = {
        (1, 'a'): 2,
        (1, 'b'): 4,
        (2, 'a'): 3,
        (2, 'b'): 4,
        (3, 'a'): 3,
        (3, 'b'): 3,
        (4, 'a'): 2,
        (4, 'b'): 3,
    }
    q0_1 = 1
    F1 = {2, 4}  
    A = dfa.DFA(Q1, Sigma1, delta1, q0_1, F1)

    Q2 = {1, 2, 3, 4}
    Sigma2 = ['a', 'b']
    delta2 = {
        (1, 'a'): 2,
        (1, 'b'): 4,
        (2, 'a'): 3,
        (2, 'b'): 4,
        (3, 'a'): 3,
        (3, 'b'): 3,
        (4, 'a'): 2,
        (4, 'b'): 3,
    }
    q0_2 = 1
    F2 = {3}  # Only state 3 is accepting
    A1 = dfa.DFA(Q2, Sigma2, delta2, q0_2, F2)
    #A1 should be equivalent to A0 if tests are correct
    #all that I did was swap the final, non initial states with non-final
    #non starting states, meaning in this case all that changes
    #is F containing 3 instead of 2, 4
    
    #testWord1 should be accepted by A and refused by A0
    #testWord2 should be accepted by A0 and refused by A
    testWords1 = ["aabababa", "ababaab", "bbaababaa"]
    testWords2 = ["ababa", "bababa", "ababababab"]

    A0 = A.refuse()

    testAutomata = [A, A1, A0]
    print("Test words 1\n")
    for automata in testAutomata:
        print(f"{automata.__repr__()}")
        for w in testWords1:
            print(f"{w}: {automata.run(w)}")
        print("\n")
    
    print("Test words 2\n")
    for automata in testAutomata:
        print(f"{automata.__repr__()}")
        for w in testWords2:
            print(f"{w}: {automata.run(w)}")
        print("\n")
        
__main__()