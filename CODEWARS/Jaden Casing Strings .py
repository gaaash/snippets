def to_jaden_case(string):
    capitalized = ""
    jadenized  = ""
    splited = string.split(" ")
    for letter in splited:

        capitalized += letter.capitalize()+" "
    jadenized = capitalized.strip()
    return jadenized
to_jaden_case("")