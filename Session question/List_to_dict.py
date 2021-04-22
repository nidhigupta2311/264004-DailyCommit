# Method 1 dict comprehension

#Reference "https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/"

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
         
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))


# Method #2 : Using zip() method

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
lst = ['one', 1, 'Two', 2, 'three', 3]
print(Convert(lst))