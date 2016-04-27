Glasses question
==

The question was posed:

    You have six glasses and a six sided die.
    When you roll the die you fill the glass corresponding to that number.
    If the glass is already full drink from the glass to empty it.
    Repeat until all glasses are full at the same time.

    How many rolls/drinks would it take to fill all the glasses at once?

This code performs that simulation and a few variants (different sized die, only match against prime numbers, etc.).

Python 2/3 compatible code, run with:

    python dice.py

Example results:

    d6, 6 glasses, matching all
                rolls      drinks
    count  100.000000  100.000000
    mean    87.180000   40.590000
    std     66.217331   33.108666
    min      6.000000    0.000000
    25%     29.500000   11.750000
    50%     76.000000   35.000000
    75%    130.000000   62.000000
    max    376.000000  185.000000

    d6, 3 glasses, matching primes
               rolls      drinks
    count  100.00000  100.000000
    mean    19.42000    3.570000
    std     19.01046    4.828901
    min      3.00000    0.000000
    25%      8.00000    1.000000
    50%     13.50000    2.000000
    75%     20.25000    4.000000
    max    100.00000   25.000000

    d10, 4 glasses, matching primes
                rolls      drinks
    count  100.000000  100.000000
    mean    53.270000    8.650000
    std     41.582061    8.335606
    min      4.000000    0.000000
    25%     20.750000    2.000000
    50%     46.000000    7.000000
    75%     72.500000   12.000000
    max    213.000000   37.000000

    d20, 8 glasses, matching primes
                 rolls      drinks
    count   100.000000  100.000000
    mean    825.040000  160.050000
    std     765.114462  152.143697
    min      20.000000    1.000000
    25%     232.750000   43.250000
    50%     586.500000  108.500000
    75%    1153.500000  227.250000
    max    3812.000000  726.000000

    d20, 12 glasses, matching composites
                  rolls        drinks
    count    100.000000    100.000000
    mean    8826.490000   2646.760000
    std     8738.411556   2625.052512
    min      122.000000     34.000000
    25%     2399.250000    719.750000
    50%     6194.000000   1871.000000
    75%    12142.000000   3619.000000
    max    41578.000000  12533.000000
