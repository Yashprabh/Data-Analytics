from scipy.stats import binom

n=10
p=0.5
k_success=2
prob_2_success = binom.pmf(k_success,n,p)
print(f"probability of 2 successes out of 10 trials: {prob_2_success}")