mport graphviz

def main():
    reg = input().strip()
    q = [[0 for _ in range(3)] for _ in range(20)]
    i = 0
    j = 1
    length = len(reg)
    nfa = graphviz.Digraph('NFA', format='png')

    while i < length:
        if reg[i] == 'a' and reg[i + 1] != '|' and reg[i + 1] != '*':
            q[j][0] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='a')
            j += 1
        if reg[i] == 'b' and reg[i + 1] != '|' and reg[i + 1] != '*':
            q[j][1] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='b')
            j += 1
        if reg[i] == 'e' and reg[i + 1] != '|' and reg[i + 1] != '*':
            q[j][2] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            j += 1

        #sanyam ends here
        if reg[i] == 'a' and reg[i + 1] == '|' and reg[i + 2] == 'b':
            q[j][2] = ((j + 1) * 10) + (j + 3)  #episolon transition
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            nfa.edge(f'q{j}', f'q{j+3}', label='e')
            j += 1
            q[j][0] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='a')
            j += 1
            q[j][2] = j + 3    #Move to the next state, update the epsilon transition in the transition table (q) for the current state (j) to the next state (j+3), and add an edge in the NFA graph from 'q{j}' to 'q{j+3}' with the label 'e' (epsilon).
            nfa.edge(f'q{j}', f'q{j+3}', label='e')
            j += 1
            q[j][1] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='b')
            j += 1
            q[j][2] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            j += 1
            i += 2
        if reg[i] == 'b' and reg[i + 1] == '|' and reg[i + 2] == 'a':
            q[j][2] = ((j + 1) * 10) + (j + 3)
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            nfa.edge(f'q{j}', f'q{j+3}', label='e')
            j += 1
            q[j][1] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='b')
            j += 1
            q[j][2] = j + 3
            nfa.edge(f'q{j}', f'q{j+3}', label='e')
            j += 1
            q[j][0] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='a')
            j += 1
            q[j][2] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            j += 1
            i += 2

            #dash ends here
        if reg[i] == 'a' and reg[i + 1] == '*':
            q[j][2] = ((j + 1) * 10) + (j + 3)
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            nfa.edge(f'q{j}', f'q{j+3}', label='e')
            j += 1
            q[j][0] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='a')
            j += 1
            q[j][2] = ((j + 1) * 10) + (j - 1)
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            nfa.edge(f'q{j}', f'q{j-1}', label='e')
            j += 1
        if reg[i] == 'b' and reg[i + 1] == '*':
            q[j][2] = ((j + 1) * 10) + (j + 3)
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            nfa.edge(f'q{j}', f'q{j+3}', label='e')
            j += 1
            q[j][1] = j + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='b')
            j += 1
            q[j][2] = ((j + 1) * 10) + (j - 1)
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            nfa.edge(f'q{j}', f'q{j-1}', label='e')
            j += 1
        if reg[i] == ')' and reg[i + 1] == '*':
            q[0][2] = ((j + 1) * 10) + 1
            nfa.edge(f'q0', f'q{j+1}', label='e')
            nfa.edge(f'q0', f'q1', label='e')
            q[j][2] = ((j + 1) * 10) + 1
            nfa.edge(f'q{j}', f'q{j+1}', label='e')
            nfa.edge(f'q{j}', f'q1', label='e')
            j += 1
        i += 1

        #manasa ends here
    print(q)

    print("\n\tTransition Table\n")
    print("_")
    print("Current State |\tInput |\tNext State")
    print("_")
    val=[]
    for i in range(j + 1):
        if q[i][0] != 0:
            print("\n  q[%d]\t      |   a   |  q[%d]" % (i, q[i][0]))
            val.append(i)
        if q[i][1] != 0:
            print("\n  q[%d]\t      |   b   |  q[%d]" % (i, q[i][1]))
            val.append(i)
        if q[i][2] != 0:
            if q[i][2] < 10:
                print("\n  q[%d]\t      |   e   |  q[%d]" % (i, q[i][2]))
                val.append(i)
            else:
                print("\n  q[%d]\t      |   e   |  q[%d] , q[%d]" % (i, q[i][2] // 10, q[i][2] % 10))
                val.append(i)

    print("_")
    print("Starting state: q",val[0],sep='')
    print("Final state: q",val[-1],sep='')

    # Save NFA diagram to a file
    nfa.render('nfa_diagram', view=True)

if name == "main":
    main()
