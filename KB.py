# Knowlegde base
KB = []


# set global KB
def set_kb(knowledge: str) -> None:
    knowledge_stms = []
    # split AND-statements
    and_stms = knowledge.split("&")
    for stm in and_stms:
        stripped = stm.replace(" ", "").replace("(", "").replace(")", "")
        new_or = stripped.split("|")
        knowledge_stms.append(new_or)

    KB.clear()
    KB.extend(knowledge_stms)


# add knowledge to global knowlegde base (KB)
def add_to_kb(knowledge: str) -> None:
    knowledge_stms = []
    # split AND-statements
    and_stms = knowledge.split("&")
    for stm in and_stms:
        stripped = stm.replace(" ", "").replace("(", "").replace(")", "")
        new_or = stripped.split("|")
        knowledge_stms.append(new_or)

    KB.extend(knowledge_stms)


# type new knowledge (CNF)
def new_knowledge() -> None:
    knowledge = input("> ")
    add_to_kb(knowledge)


def pl_resolution(KB: list, alpha: str) -> bool:
    # nagate alpha
    if "!" in alpha:
        alpha = alpha[1:]
    else:
        alpha = "!" + alpha

    # put alpha in a list
    alpha_as_list = []
    alpha_as_list.append(alpha)

    # clauses = KB + !alpha
    clauses = KB
    clauses.append(alpha_as_list)

    new = []

    while(True):
        # making temp array
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                resolvents = pl_resolve(clauses[i], clauses[j])
                # contains the empty clause
                if not resolvents:
                    return True
                if resolvents not in new:
                    new.append(resolvents)

        # check if new is a subset of clauses
        if all(x in clauses for x in new):
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
                    m_set.remove(c_i)
                    m_set.remove(c_j)
            # c_j is negated, but not c_i
            elif "!" not in c_i and "!" in c_j:
                if c_i == c_j[1:]:
                    m_set.remove(c_i)
                    m_set.remove(c_j)

    # returning unique list. Fx [b, b] -> [b]
    return list(set(m_set))


###################################
#
#       TO RUN THE PROGRAM
#
###################################
test_kb = "(!a | b) & a & !b"
# "(!d | b) & a & !g"

set_kb(test_kb)

add_to_kb("!d")

alpha = "!b"
if pl_resolution(KB, alpha):
    print("KB entails alpha")
else:
    print("KB does *NOT* entail alpha")
