
def main():
    nums = [200, 99, 98, 100, 97, 100, 200]
    index_of_item(nums)


# returns the position/index of the first occurrence of an item in a list
def index_of_item(nums):
    user_input = int(input("Enter a enter to find its index: "))

    if user_input in nums:
        print("The number is registered and its index is:", nums.index(user_input))
    else:
        print('Sorry the number is not in our records')


if __name__ == '__main__':
    main()