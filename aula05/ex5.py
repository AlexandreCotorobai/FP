
matches = []
equipas = ['FCP', 'SCP', 'SLB']


def matching(equipas):

    n = 0
    for i in equipas:
        for j in equipas:
            if i != j:
                matches.append((i, j))
                n += 1
    print(matches)
            


matching(equipas)