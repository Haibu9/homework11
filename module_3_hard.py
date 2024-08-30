


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    x = 0
    for i in range(0, len(data_structure)):
        ward = data_structure[i]
        if isinstance(ward, int) == True or isinstance(ward, float) == True:
            x += ward
        elif isinstance(ward, str) == True:
            x += len(ward)
        elif isinstance(ward, list) == True or isinstance(ward, tuple) == True:
            x += calculate_structure_sum(ward)
        elif isinstance(ward, dict) == True:
            b = list(ward.keys())
            c = list(ward.values())
            x += calculate_structure_sum(b)
            x += calculate_structure_sum(c)
        elif isinstance(ward, set) == True:
            x += calculate_structure_sum(list(ward))
    return x

print(calculate_structure_sum(data_structure))
