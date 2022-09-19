print_list = []
def input_print(value):
    count = value.__len__()
    length = count * 3
    side = length + 10
    input_string = ""
    for i in value:
        a = i
        
    f_p = int((a / 20) + 1)
    t_p = a % 20
    print_list.append([f_p, t_p])
