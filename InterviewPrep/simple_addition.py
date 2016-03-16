"""

Given an array an a number add it in such a way where if the array is [0,0,1]
and you add 10, you get [0, 1, 1]. If you add 9 to [1] you get [1, 0]

"""

def add_num_to_array(array, num):

    carry = num
    for ii in range(len(array), 0, -1):
        val = array[ii-1] + carry
        array[ii-1] = val % 10
        carry = int(val / 10)


    while carry != 0:
        array = [carry % 10] + array
        carry = int(carry / 10)

    print(array)


array = [0,0,1]
num = 4
add_num_to_array(array, num)
