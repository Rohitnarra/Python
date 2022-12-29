def find_num(number_list: list, number: int)->bool:
 for iterate_number in number_list:
    if iterate_number == number:
        return True
    else:
        #pass
        return False
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

# The above code will return None when the function has nothing to return, to make it return False, we used return False statement.
# It will return True if the parmeter value number is found in the parameter list values.