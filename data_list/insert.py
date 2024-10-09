
def main():
    nums = [200, 99, 98, 100, 97, 100, 200]
    insert_item(nums)
    print(nums)


def insert_item(nums):
    user_input = int(input("Enter your preferred reference: "))

    nums.insert(1, user_input)
    print("Your reference has been added at index 1 of the list")


if __name__ == '__main__':
    main()