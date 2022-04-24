class not_int(Exception):
    pass
#
# def calc(*args):
#     result = 0
#     for el in args:
#         try:
#             if isinstance(el, int):
#                 result += el
#             else:
#                 raise not_int
#
#         except not_int:
#             raise not_int(f'Element {el} is not an integer.')
#     return result


def calc2(*args):
    if any(x for x in args if isinstance(x, float)):
        raise not_int(f'There is an element which is not an integer.')
    return sum(x for x in args if isinstance(x, int))




print(calc2(1, 2, 3, 4, 5.5))