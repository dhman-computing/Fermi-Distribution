# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-using-enumerate
# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=consider-using-f-string
# pylint: disable=trailing-whitespace
# pylint: disable=no-member
# pylint: disable=missing-function-docstring

from support1 import n_dimensional_monte_carlo_integration as ndmci
from support1 import xy as f
from support1 import xyz as f1
from cProfile import run

def main():
    xlimit = [[0, 2], [0, 2], [0, 2]]
    N = 10**5 #int(input("No of random points to be considered : "))

    answer = 8 # float(input("Correct Answer : "))

    integration = ndmci(f1, xlimit, N)
    perror = 100 * (answer - integration) / answer
    
    print(f"Result : {integration}")
    print(f"Rounded Result : {round(integration, 3)}")
    print(f"Percentage Error : {perror}%")
    return integration, perror

# run("main()")
itteration = 1000
i = [0 for _ in range(itteration)]
e = [0 for _ in range(itteration)]

for j in range(itteration):
    print(f"Interation : {j + 1}")
    i[j], e[j] = main()
    
avi = sum(i) / itteration
ave = sum(e) / itteration

print(f"Average Result : {avi}")
print(f"Average Rounded Result : {round(avi, 3)}")
print(f"Average Percentage Error : {ave}%")
