'''
Функция перевода IP/маски в двоичный формат
'''
def data_to_binary(data):
    data_list_bin = []
    res_lst = []
    data_list = data.split(".")

    for oct in data_list:
        oct = int(oct)
        data_list_bin.append(bin(oct)[2:])

    for i in data_list_bin:
        if len(i) < 8:
            lngth = 8 - len(i)
            while lngth != 0:
                i = "0" + i
                lngth -= 1
            res_lst.append(i)
        else:
            res_lst.append(i)

    return res_lst
