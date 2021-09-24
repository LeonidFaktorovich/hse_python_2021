def decor(func):
    def reversing(obj_1, obj_2):
        new_obj_1 = obj_1[::-1]
        new_obj_2 = obj_2[::-1]
        return func(new_obj_1, new_obj_2)

    return reversing


@decor
def numbers(obj_1, obj_2):
    return int(obj_1) + int(obj_2)


@decor
def strings(obj_1, obj_2):
    if obj_1 >= obj_2:
        return [obj_2, obj_1]
    else:
        return [obj_1, obj_2]


obj_1 = input()
obj_2 = input()
if obj_1.isdigit() and obj_2.isdigit():
    print(numbers(obj_1, obj_2))
else:
    print(*strings(obj_1, obj_2))
