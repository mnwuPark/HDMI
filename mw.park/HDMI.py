from tkinter.tix import Tree


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

    for i in range(20):
        i += 1
        j = int(i / 20) + 1
        k = i % 20
        f = [j, k]
        if f in print_list:
            input_string += "■"
            if i % 20 == 0:
                print(input_string)
                input_string = ""
        else:
            input_string += "□"
            if i % 20 == 0:
                print(input_string)
                input_string = ""

output_string = '''

#################################
#                               #
#                               #
#          OUTPUT : {}          #
#                               #
#                               #
#################################

'''

input_string = " INPUT : {} LIST {} "

st_list = []

while True:
    scan = input("input : ")

    if "input" in scan:
        add = scan[6:]
        if int(add) > 20:
            print("값을 초과하였습니다.")
            break
        elif int(add) < 1:
            print("값이 너무 작습니다.")
            break
        
        try:
            int_add = int(add)
        except Exception as e:
            print("Error")
            print(e)
            break

        if int_add in st_list:
            print("이미 입력된 값입니다.")
        else:
            st_list.append(int_add)
            input_print(st_list)
            print(st_list)
