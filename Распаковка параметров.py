def print_params(a: object = 1, b: object = 'Anar', c: object = True) -> object:
    print(a, b, c)


#роспакоука...
values_list = [7, False, "human"]
values_dict = {"a": 85, "b": True, "c": "A"}
values_list2 = [23, "years"]
print_params(2, 5)
print_params("Askerov")
print_params(b=25)
print_params(c=[1,2,3])
print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)




