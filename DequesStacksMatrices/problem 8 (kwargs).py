def start_spring(**kwargs):
    result_dict = {}

    for key,value in kwargs.items():
        name_of_object = key
        object_type = value
        if not object_type in result_dict.keys():
            result_dict[object_type] = [name_of_object]
        else:
            result_dict[object_type] += [name_of_object]
    result = ""
    for key,value in sorted(result_dict.items(), key = lambda y: (-len(y[1]), y[1])):
        result += f"{key}:\n"

        for x in sorted(value):
            result += f"-{x}\n"

    return result