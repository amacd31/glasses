import pandas as pd
import numpy as np

def simulate(max_iter):
    glasses = np.array([ False ] * 6)
    drinks = 0
    for count in range(1, max_iter + 1):
        chosen_glass = np.random.randint(0, 6)
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

def get_dist(num_samples, max_iter):
    """
        num_samples: number of samples to produce.
        max_iter: total number of iterations to attempt before giving up on a particular sample.
    """
    rolls = []
    drinks = []
    for i in range(num_samples):
        roll_count, drink_count = simulate(max_iter)
        rolls.append(roll_count)
        drinks.append(drink_count)

    return rolls, drinks

sampled = pd.DataFrame(
    np.array(
        get_dist(100000,2000)
    ).T,
    columns = ['rolls', 'drinks']
)

print(sampled.describe())
