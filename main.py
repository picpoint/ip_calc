print("Программа показывающая подсеть по маске")
print("---------------------------------------")
ip = input("Введите IP адресс: ")
mask = input("Введите маску: ")

'''
Функция перевода IP в двоичный формат
'''
def ip_to_binary(ip):
    ip_list_bin = []
    res_lst = []
    ip_list = ip.split(".")

    for oct in ip_list:
        oct = int(oct)
        ip_list_bin.append(bin(oct)[2:])

    for i in ip_list_bin:
        if len(i) < 8:
            lngth = 8 - len(i)
            while lngth != 0:
                i = "0" + i
                lngth -=1
            res_lst.append(i)
        else:
            res_lst.append(i)

    return res_lst


'''
Функция перевода маски в двоичный формат
'''
def mask_to_binary(mask):
    mask_list = mask.split(".")
    mask_list_binary = []
    res_mask_list_binary = []

    for i in mask_list:
        oct = bin(int(i))
        mask_list_binary.append(oct[2:])

    for oct in mask_list_binary:
        while len(oct) < 8:
            oct = "0" + oct
        res_mask_list_binary.append(oct)
    return res_mask_list_binary


ip_list = ip_to_binary(ip)
mask_list = mask_to_binary(mask)



def apply_mask_to_ip(ip, mask):
    print(ip)
    print(mask)
    counter_bit = 0
    ip_bin_str = ""
    network_ip = ""
    host_ip = ""

    for oct_mask in mask:
        for bit_mask in oct_mask:
            # print(bit_mask)
            if bit_mask == "1":
                counter_bit += 1
    print(counter_bit)

    for oct_ip in ip:
        for bit_ip in oct_ip:
            ip_bin_str += bit_ip

    print(ip_bin_str)

     





apply_mask_to_ip(ip_list, mask_list)
