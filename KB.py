# Knowlegde base
KB = [['b'], ['!b', 'c', 'k'], ['!l'], ['!c']]
#    [['b'], ['!b', 'c'], ['!l'], ['c']]
#    [['c'], ['!l']]


# add knowledge to global knowlegde base (KB)
def add_to_kb(knowledge: str) -> None:
    knowledge_stms = []
    # split AND-statements
    and_stms = knowledge.split("&")
    for stm in and_stms:
        stripped = stm.replace(" ", "").replace("(", "").replace(")", "")
        new_or = stripped.split("|")
        knowledge_stms.append(new_or)

    KB.append(knowledge_stms)


# type new knowledge (CNF)
def new_knowledge() -> None:
    knowledge = input("> ")
    add_to_kb(knowledge)


'''
KB = [['b'], ['!b', 'c'], ['!l']]
     [['b'], ['!b', 'c'], ['!l'], ['c']]
     [['c'], ['!l']]
'''


def pl_resolution(KB: list) -> bool:
    # if "!" in a:
    #     a = a[1:]
    # else:
    #     a = "!" + a

    clauses = KB
    new = []

    while(True):
        # making temp array
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                print(f"c1={clauses[i]} og c2={clauses[j]}")
                resolvents = pl_resolve(clauses[i], clauses[j])
                print(f"resolvents: {resolvents}")
                # contains the empty clause
                if not resolvents:
                    print("har empty list")
                    return True
                if resolvents not in new:
                    new.append(resolvents)

        # check if new is a subset of clauses

        if all(x in clauses for x in new):
            print("her")
            return False

        # clauses union new
        for new_clause in new:
            if new_clause not in clauses:
                clauses.append(new_clause)


# check if the two inputs are each others complement
def pl_resolve(clause1: list, clause2: list) -> list:
    # combining the two clauses
    m_set = clause1 + clause2

    # removing when we find a compliment (two opposites)
    for c_i in clause1:
        for c_j in clause2:
            # c_i is negated, but not c_j
            if "!" in c_i and "!" not in c_j:
                if c_i[1:] == c_j:
                    print(f"1: c_i: {c_i} og c_j: {c_j} og m_set: {m_set}")
                    m_set.remove(c_i)
                    m_set.remove(c_j)
            # c_j is negated, but not c_i
            elif "!" not in c_i and "!" in c_j:
                if c_i == c_j[1:]:
                    print(f"2: c_i: {c_i} og c_j: {c_j} og m_set: {m_set}")
                    m_set.remove(c_i)
                    m_set.remove(c_j)

    # returning unique list. Fx [b, b] -> [b]
    return list(set(m_set))


# new_knowledge()
hej = [["!a", "b"], ["a"], ["!c"]]
pl_resolution(hej)

print(pl_resolve(["!b", "a"], ["b", "!a"]))
#print(f"KB: {KB}")


'''
hej = "A & (b | c) & ba | r"
add_to_kb(hej)

hej2 = "k &hej & (t| e)"
add_to_kb(hej2)
'''
