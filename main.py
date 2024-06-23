print("Программа показывающая подсеть по маске")
print("---------------------------------------")
ip = input("Введите IP адресс: ")
mask = input("Введите маску: ")

def ip_to_binary(ip):
    ip_list_bin = []
    res_lst = []

    # print(ip)
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


def mask_to_binary(mask):
    # print(mask)
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

apply_mask_to_ip(ip_list, mask_list)

print()
