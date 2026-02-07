list =[1,3,5,9]

def first_even_num(list):
    for n in list:
        if n % 2 == 0:
            return n
    return None
print(first_even_num(list))