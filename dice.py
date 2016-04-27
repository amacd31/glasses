import pandas as pd
import numpy as np

class Simulate(object):
    def __init__(self, die_size, num_glasses, select_glass = None):
        self.die_size = die_size
        self.num_glasses = num_glasses
        if select_glass is not None:
            self.select_glass = select_glass
        else:
            self.select_glass = lambda die_roll: die_roll

    def simulate(self, max_iter):
        glasses = np.array([ False ] * self.num_glasses)
        drinks = 0
        for count in range(1, max_iter + 1):
            die_roll = np.random.randint(0, self.die_size)
            chosen_glass = self.select_glass(die_roll)
            if chosen_glass is not None:
                # If full then drink
                if glasses[chosen_glass]:
                    # Emptying the glass
                    glasses[chosen_glass] = False
                    drinks += 1
                else:
                    # Else the glass was empty, so fill it
                    glasses[chosen_glass] = True

            # If all the glasses are full i.e. True
            if np.alltrue(glasses):
                # Return the count of dice rolls/iterations.
                return count, drinks

        # We didn't manage to fill all the glasses at once in less
        # than max_iter iterations, so pass back a missing value.
        return np.nan, drinks

    def get_dist(self, num_samples, max_iter):
        """
            num_samples: number of samples to produce.
            max_iter: total number of iterations to attempt before giving up on a particular sample.
        """
        rolls = []
        drinks = []
        for i in range(num_samples):
            roll_count, drink_count = self.simulate(max_iter)
            rolls.append(roll_count)
            drinks.append(drink_count)

        return rolls, drinks

def d20_match_prime(die_roll):
    for i, prime in enumerate([1,3,5,7,11,13,17,19]):
        if i + 1 == die_roll:
            return i

    return None

def d20_match_composite(die_roll):
    for i, prime in enumerate([2,4,6,8,9,10,12,14,15,16,18,20]):
        if i + 1 == die_roll:
            return i

    return None

def d10_match_prime(die_roll):
    for i, prime in enumerate([1,3,5,7]):
        if i + 1 == die_roll:
            return i

    return None

def d6_match_prime(die_roll):
    for i, prime in enumerate([1,3,5]):
        if i + 1 == die_roll:
            return i

    return None

num_simulations = 100
max_iters = 100000

sim = Simulate(6,6)
sampled = pd.DataFrame(
    np.array(
        sim.get_dist(num_simulations, max_iters)
    ).T,
    columns = ['rolls', 'drinks']
)
print('')
print('d6, 6 glasses, matching all')
print(sampled.describe())

sim = Simulate(6,3, d6_match_prime)
sampled = pd.DataFrame(
    np.array(
        sim.get_dist(num_simulations, max_iters)
    ).T,
    columns = ['rolls', 'drinks']
)
print('')
print('d6, 3 glasses, matching primes')
print(sampled.describe())

sim = Simulate(10,4, d10_match_prime)
sampled = pd.DataFrame(
    np.array(
        sim.get_dist(num_simulations, max_iters)
    ).T,
    columns = ['rolls', 'drinks']
)
print('')
print('d10, 4 glasses, matching primes')
print(sampled.describe())

sim = Simulate(20,8, d20_match_prime)
sampled = pd.DataFrame(
    np.array(
        sim.get_dist(num_simulations, max_iters)
    ).T,
    columns = ['rolls', 'drinks']
)

print('')
print('d20, 8 glasses, matching primes')
print(sampled.describe())

sim = Simulate(20,12, d20_match_composite)
sampled = pd.DataFrame(
    np.array(
        sim.get_dist(num_simulations, max_iters)
    ).T,
    columns = ['rolls', 'drinks']
)

print('')
print('d20, 12 glasses, matching composites')
print(sampled.describe())

