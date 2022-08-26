'''
function should accept a variable number of input arguments representing the number of sides on an arbitrary number of dice, 
and its output should print a table of the probability for each possible outcome
'''

import random
import matplotlib.pyplot as pp

def dice_sides(dice1, dice2):
    if dice1 == 4 and dice2 == 6:
        trials_list = []
        for i in range(5000000):
            trials_outcomes = random.randint(1, dice1) + random.randint(1, dice2)
            trials_list.append(trials_outcomes)
        print(f'loop ran {i} times')
        
        unique_trials_list = set(trials_list)
        unique_trials_list = list(unique_trials_list)
        probability_list = []

        print('Outcome\tProbability')
        for i in range(len(unique_trials_list)):
            if unique_trials_list[i] in trials_list:
                probability = trials_list.count(unique_trials_list[i]) / len(trials_list)
                probability_list.append(probability)
                print(f'{unique_trials_list[i]}: \t{round(probability,2) * 100}%')
        
        pp.plot(unique_trials_list, probability_list)

    elif dice1 == 6 and dice2 == 6:
        trials_list = []
        for i in range(5000000):
            trials_outcomes = random.randint(1, 6) + random.randint(1, 6)
            trials_list.append(trials_outcomes)
        print(f'loop ran {i} times')
        
        unique_trials_list = set(trials_list)
        unique_trials_list = list(unique_trials_list)
        probability_list = []

        print('Outcome\tProbability')
        for i in range(len(unique_trials_list)):
            if unique_trials_list[i] in trials_list:
                probability = trials_list.count(unique_trials_list[i]) / len(trials_list)
                probability_list.append(probability)
                print(f'{unique_trials_list[i]}: \t{round(probability,2) * 100}%')
        
        pp.bar(unique_trials_list, probability_list)

    elif dice1 == 4 and dice2 == 4:
        trials_list = []
        for i in range(5000000):
            trials_outcomes = random.randint(1, dice1) + random.randint(1, dice2)
            trials_list.append(trials_outcomes)
        print(f'loop ran {i} times')
        
        unique_trials_list = set(trials_list)
        unique_trials_list = list(unique_trials_list)
        probability_list = []

        print('Outcome\tProbability')
        for i in range(len(unique_trials_list)):
            if unique_trials_list[i] in trials_list:
                probability = trials_list.count(unique_trials_list[i]) / len(trials_list)
                probability_list.append(probability)
                print(f'{unique_trials_list[i]}: \t{round(probability,2) * 100}%')
        
        pp.plot(unique_trials_list, probability_list)

        
        
dice_sides(6,6)
