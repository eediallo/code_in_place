
def main():
    nums = []
    is_list_empty(nums)


def is_list_empty(nums):
    if nums:
        print('Nums has elements in it 😊😊😊😊 \nAnd here they are:')
    for num in nums:
        print(num)
    else:
        print("nums does not have elements in it.😒😒😒😒 ")
    


if __name__ == '__main__':
    main()