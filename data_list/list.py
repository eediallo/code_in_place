




def main():
    nums = [12, 6, 34, 99, 90, 20, 30, 99, 12]

    # change_values add the value 42 at the add of nums
    change_value(nums)
    print(print_nums(nums))

    new_nums = multiply_by_two(nums)

    print(new_nums)



# takes an array and print each item of it
def print_nums(nums):
      for i in range(len(nums)):
        print(i, ':', nums[i])


# takes an array and multiply each item of the array by two
def multiply_by_two(nums):
    new_nums = []
    for i in range(len(nums)):
         new_nums.append(nums[i]*2)
    new_nums.pop(len(new_nums)-1)
    if 12 in new_nums:
        print('Youpiiiiiiiiiiiiiiii 12 is thereeeeeeeeeee 😊😊😊😊😊😊 ')
    else:
        print('oooopp!!!!!!!!!!! 12 is not thereeeeeeeeeeeeeee!')
    return new_nums


def change_value(nums):
    nums.append(42)



def is_list_empty(nums):
    if nums:
        print('Nums has elements in it')
    else:
        print("nums does not have elements in it.😒😒😒😒 ")
    


# execute main function when this file is executed
if __name__=='__main__':
    main()



