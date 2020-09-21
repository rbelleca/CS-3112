import random
import itertools

def toss_coin():
    """ 
    Function: Will return either 'H' or 'T'. Basically, tossing a coin
    """
    decider = random.randrange(2)
    if (decider == 1): return 'H'
    else : return 'T'

def simulate_toss_coins(n, m=2, p=0):
    """
    n = number of toss
    m = number of coins
    p = number of head/tails shown
    """

    numberOfCoins = list()
    count = list()
    #Create list for each number of coin
    for x in range(m):
        numberOfCoins.append(list())
        count.append(list())
        count[x] = 0   

    #Simulate coin toss n number of times
    for i in range(n):
        for j in range(len(numberOfCoins)):
            numberOfCoins[j].append(toss_coin())
    
    #Compare tosses from each list
    r = list(range(p))
    isThereHead = False
    for i in range(len(numberOfCoins[0])): #Horizontal
        for j in range(1, len(numberOfCoins)): 
            if (numberOfCoins[j][i] == 'H'):
                count[j] += 1
                isThereHead = True
        if (isThereHead == False): count[0] += 1
                
    print(f'count: {count}')

    show_possibilities(numberOfCoins)

    # rf_2 = ('%2.2f' % ((heads_2/30)*100))
    # rf_1 = ('%2.2f' % ((heads_1/30)*100))
    # rf_0 = ('%2.2f' % ((heads_0/30)*100))


def get_possible_outcomes(l,n=1):
    """ 
    Function: will list all possible outcomes of the list with minimum n number of elements.
    Input: l = list of the possible single outcome, n = number of toss
    For ex: l = ['H', 'T'], n = 2 will give you all the possible outcomes of tossing a coin twice.
    """
    return list(itertools.product(l, repeat=n))

def get_exactly_events(possibilities, s, n=0):
    count = list()

    for x in possibilities:
        if (x.count(s) == n): 
            count.append(x)

    print(f'\nExactly {n} occurence of {s}')
    print(f'probability: {len(count)}{"/"}{len(possibilities)}')
    print(f'relative probability: {(len(count)/len(possibilities))*100}')

    return count

def get_atleast_events(possibilities, s, n=0):
    count = list()

    for x in possibilities:
        if (x.count(s) >= n): 
            count.append(x)

    print(f'\nAt least {n} occurence of {s}')
    print(f'probability: {len(count)}{"/"}{len(possibilities)}')
    print(f'relative probability: {(len(count)/len(possibilities))*100}')

    return count

def show_possibilities(possibilities):
    count=0
    for x in possibilities:
        count += 1
        print(x, flush='True')
    
    return count
    


# #First ball is blue
# pos = get_possible_outcomes(['B1', 'B2', 'W1', 'W2', 'W3'], n=2)
# # show_possibilities(pos)

# count = 0
# for x in pos:
#     if (x[0] in ['W1', 'W2', 'W3'] and x[1] in ['W1', 'W2', 'W3']):
#         print(x)
#         count += 1
# print(count)
# print(len(pos))

pos = get_possible_outcomes(['H', 'T'], n=4)
show_possibilities(pos)

print(get_exactly_events(pos, 'H', 1))