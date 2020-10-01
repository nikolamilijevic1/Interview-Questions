# Given a function that outputs a real number from 0-1 at random, calculate pi

import sys
import math
import random

def estimate_pi():
    while 1:
        trials = int(input("Enter the number of trials you wish to perform: "))
        trial_succeses = 0.0
        for _ in range(trials):
            x_coord = random.uniform(0,1)
            y_coord = random.uniform(0,1)
            distance = math.sqrt(x_coord**2 + y_coord**2)
            if distance <= 1:
                trial_succeses += 1.0

        pi_estimate = "{:.6f}".format(4 * trial_succeses / trials)
        print pi_estimate,"\n"

if __name__ == '__main__':
    globals()[sys.argv[1]]()
