def gale_shapley(male_prefs: list, female_prefs: list) -> list[tuple]:
    mp = {male: pref for male, pref in male_prefs}

    males = male_prefs
    # We hash the index pointer for each male to kee track of their curr/ex engagement, increments by one if they are rejected for another
    # male
    curr_pair = {male: 0 for male, _ in male_prefs}
    fp = {}

    # -1 indicates the female is free, we hash the rankings of their preferences for easier reference and save the current male
    # they are engaged to
    for female, pref in female_prefs:
        fp[female] = [{male: rank for rank, male in enumerate(pref)}, (-1, None)]

    iteration = 0
    while males:
        print(f"Iteration {iteration}")

        temp = []
        for male, pref in males:
            pointer = curr_pair[male]
            female = pref[pointer]
            # If the female is free, we simply assign her to that male
            if fp[female][1][0] == -1:
                fp[female][1] = (fp[female][0][male], male)
            # If she isn't free and the current male is preferred, reject her current engagement and replace him
            elif fp[female][1][0] != -1 and fp[female][0][male] < fp[female][1][0]:
                free_male = fp[female][1][1]
                temp.append((free_male, mp[free_male]))
                curr_pair[free_male] += 1
                fp[female][1] = (fp[female][0][male], male)
            # Other add the rejected male to the list and go down his preference list
            else:
                temp.append((male, mp[male]))
                curr_pair[male] += 1

        males = temp
        iteration += 1
        print(f"Current pairings: {[(fp[fem][1][1], fem) for fem in fp if fp[fem][1][0] != -1]}")
    
    pairings = [(male, pref[curr_pair[male]]) for male, pref in male_prefs]
    print("Derived pairings:")
    for pair in pairings:
        print(pair)
    return pairings

if __name__ == '__main__':
    male_prefs = [
        ('A', tuple("OMNLP")),
        ('B', tuple("PNMLO")),
        ('C', tuple("MPLON")),
        ('D', tuple("PMONL")),
        ('E', tuple("OLMNP")),
    ]
    female_prefs = [
        ('L', tuple("DBECA")),
        ('M', tuple("BADCE")),
        ('N', tuple("ACEDB")),
        ('O', tuple("DACBE")),
        ('P', tuple("BEACD")),
    ]
    pairings = gale_shapley(male_prefs, female_prefs)
