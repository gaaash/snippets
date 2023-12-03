def narcissistic( value ):
    nums_list = []
    new_value = 0
    value_shiti = value # i had problem with local variable so i assign it here :(
    while value_shiti != 0:
        num = value_shiti % 10
        nums_list.append(num)
        value_shiti //= 10
    for i in nums_list:
        new_value += pow(i,len(nums_list))
    if new_value == value:
        return True    
    else :
        return False

narcissistic(4887)