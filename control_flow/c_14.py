
import math 

K = -8266.64

def main():
    calculate_age_single_sample()
    print('')


# calculate the age of a sample based on the is c14
def calculate_age_single_sample():
    pct_left = float(input(" % of natural c14: "))
    age = K * math.log(pct_left / 100)

    print("sample is", str(age), "years old")



if __name__ == '__main__':
    main()