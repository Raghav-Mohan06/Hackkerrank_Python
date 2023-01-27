def count_substring(string, sub_string):
    counter = 0
    for i,c in enumerate(string):
        if i + len(sub_string) > len(string):
            break
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
    return counter

