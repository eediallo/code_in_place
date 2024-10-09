
def main():
    print_first_100_even_nums()



def print_first_100_even_nums():
    for i in range(100):
        if (i % 2 == 0):
            print(i)



if __name__ == '__main__':
    main()