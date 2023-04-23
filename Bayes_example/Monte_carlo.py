from bayes import main
import numpy as np
import time

def double_down(p1,p2,p3):
    ## take probabilities and choose largest probability selection
    if p1 > p2 and p1 > p3:
        return "1"
    elif  p2 > p1 and p2 > p3:
        return "2"
    else:
        return "3"

def top_two(p1,p2,p3):
    if p1 < p2 and p1 < p3:
        return "6"
    elif  p2 < p1 and p2 < p3:
        return "5"
    else:
        return "4"


start_t=time.perf_counter()


#how many trials will be used to compare algorithms
num_iter=100

trials=np.zeros(num_iter)

#Checking the doubling down method

for i in range(len(trials)):
    trials[i]=main(double_down)
    #print("This iteration took " + str(trials[i]) + " iterations")
mean_alg1=np.mean(trials)
std_alg1=np.std(trials)

#Checking the splitting up method

for i in range(len(trials)):
    trials[i]=main(top_two)
    #print("This iteration took " + str(trials[i]) + " iterations")
mean_alg2=np.mean(trials)
std_alg2=np.std(trials)

end_t=time.perf_counter()


print("\nBelow are the average number of searches required by a search algorithm to find the missing boater\n")
print("Doubling up: " + str(mean_alg1)+ " searches (standard deviation of " + str(std_alg1)+")")
print("Splitting up: " + str(mean_alg2)+ " searches (standard deviation of " + str(std_alg2)+")")
print("\nThis code took " + str((end_t-start_t)/60) + " minutes to run.")



