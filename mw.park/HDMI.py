print_list = [[1, 1]]

def input_print(value):
    count = value.__len__()
    length = count * 3
    side = length + 10
    input_string = ""
    for i in value:
        a = i

    f_p = int((a / 8) + 1)
    t_p = a % 8
    print_list.append([f_p, t_p])

    for i in range(8):
        i += 1
        j = int(i / 8) + 1
        k = i % 8
        f = [j, k]
        if f in print_list:
            input_string += "■"
            if i % 8 == 0:
                print(input_string)
                input_string = ""
        else:
            input_string += "□"
            if i % 8 == 0:
                print(input_string)
                input_string = ""

output_string = '''

#################################
#                               #
#                               #
#          OUTPUT : {}           #
#                               #
#                               #
#################################

'''

input_string = " INPUT : {} LIST {} "

st_list = [1]

while True:
    scan = input("input : ")

    if "input" in scan:
        add = scan[6:]
        if int(add) > 8:
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
            print("OUTPUT Value : {}".format(st_list[-1]))

    elif "output" in scan:
        sub = scan[7:]
        if int(sub) > 8:
            print("값을 초과하였습니다.")
            break
        elif int(sub) < 1:
            print("값이 너무 작습니다.")
            break
        
        try:
            int_sub = int(sub)
        except Exception as e:
            print("Error")
            print(e)
            break

        if int_sub in st_list:
            st_list.remove(int_sub)
            print(st_list)
            print(output_string.format(st_list[-1], st_list))
            
            j = int(int_sub / 8) + 1
            k = int_sub % 8
            print_list.remove([j, k])

        else:
            print("존재하지 않는 값입니다.")

    elif "status" in scan:
        print("현재 활성되어 있는 코드 : {}".format(st_list))
        print("OUTPUT Value : {}".format(st_list[-1]))

    else:
        print("잘못된 값입니다.")