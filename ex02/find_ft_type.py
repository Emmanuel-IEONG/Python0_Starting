def all_thing_is_obj(object: any) -> int:
    types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "Str"
    }

    object_type = type(object)
    type_name = types.get(object_type, "Type not found")

    if object_type is str:
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name != "Type not found":
        print(f"{type_name} : {object_type}")
    else:
        print(type_name)

    return (42)
