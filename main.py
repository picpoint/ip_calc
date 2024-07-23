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
                lngth -= 1
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

'''
Функция наложения маски на IP и вычисления
'''
def apply_mask_to_ip(ip, mask):
    # print(ip)
    # print(mask)
    counter_bit_mask = 0
    ip_bin_str = ""
    network_ip = ""
    host_ip = ""

    for oct_mask in mask:
        for bit_mask in oct_mask:
            # print(bit_mask)
            if bit_mask == "1":
                counter_bit_mask += 1
    # print(counter_bit_mask)

    for oct_ip in ip:
        for bit_ip in oct_ip:
            ip_bin_str += bit_ip

    print()
    # print(f"IP в строке - {ip_bin_str}")
    # print(f"Длинна маски {counter_bit_mask}")
    network_adress_part = ip_bin_str[:counter_bit_mask]
    # print(f"Network Adress - {network_adress_part}")
    host_adress_binary_part = ip_bin_str[counter_bit_mask:len(ip_bin_str)]
    # print(f"Host adress - {host_adress_binary_part}")

    full_network_adress_bin = network_adress_part
    for i in range(0, 32 - len(network_adress_part)):
        full_network_adress_bin += "0"

    # print(f"Full NA bin - {full_network_adress_bin}")

    full_network_adress_bin_list = []
    counter = 0
    tmp = ""
    network_adress = ""

    for i in full_network_adress_bin:
        tmp += i
        counter += 1
        if counter == 8:
            full_network_adress_bin_list.append(tmp)
            counter = 0
            tmp = ""

    for i in full_network_adress_bin_list:
        octet = int(i, 2)
        network_adress = network_adress + str(octet) + "."

    network_adress = network_adress[:-1]
    print(f"Адрес сети - {network_adress}")
    print(f"Длинна маски - {counter_bit_mask}")

    # host_adress_binary_part
    # host = "0000000001111011"
    # print(host)

    revrs_host = host_adress_binary_part[::-1]
    # print(revrs_host)

    counter_octet = 0
    tmp_list = ""
    host_list = []

    for i in revrs_host:
        counter_octet += 1
        tmp_list += i
        if len(tmp_list) == 8:
            host_list.append(tmp_list)
            tmp_list = ""
        if len(tmp_list) < 8 and counter_octet == len(host_adress_binary_part):
            host_list.append(tmp_list)

    # print(host_list)

    host_ip_list = []
    host_ip_dec = ''

    for i in host_list:
        if i != '':
            octet_ip = i[::-1]
            octet_ip = int(octet_ip, 2)
            host_ip_list.insert(0, octet_ip)

    for i in host_ip_list:
        host_ip_dec = host_ip_dec + str(i) + '.'

    host_ip_dec = host_ip_dec[:len(host_ip_dec) - 1]
    print(f"Адрес хоста - {host_ip_dec}")

    hosts_in_network = 2 ** (len(host_adress_binary_part)) - 2
    print(f"Количество хостов в сети - {hosts_in_network}")

    '''
    вычисление broadcast адреса
    '''
    network_adress_part_bin = full_network_adress_bin[:counter_bit_mask]
    # print(f"Часть адреса сети - {network_adress_part_bin}")

    for i in range(0, 32 - counter_bit_mask):
        network_adress_part_bin += "1"

    broadcast_full_adress_bin = network_adress_part_bin
    # print(broadcast_full_adress_bin)

    counter_broadcast_octet = 0
    broadcast_full_adress_list = []
    tmp = ""

    for i in broadcast_full_adress_bin:
        counter_broadcast_octet += 1
        if counter_broadcast_octet <= 8:
            tmp += i
            if counter_broadcast_octet == 8:
                broadcast_full_adress_list.append(tmp)
                tmp = ""
                counter_broadcast_octet = 0

    # print(broadcast_full_adress_list)
    broadcast_adress = ""

    for i in broadcast_full_adress_list:
        broadcast_adress = broadcast_adress + str(int(i, 2)) + "."
    broadcast_adress = broadcast_adress[:-1]
    print(f"Широковещятельный адрес - {broadcast_adress}")


    '''
    Вычисление начального адреса хоста
    '''
    host_min_bin = full_network_adress_bin[:len(full_network_adress_bin) - 1]
    host_min_bin += "1"
    tmp = ""
    min_host_list_bin = []
    min_host = ""
    counter_octet_bin = 1
    for i in host_min_bin:
        if counter_octet_bin <= 8:
            tmp += i
            counter_octet_bin += 1
            if counter_octet_bin == 9:
                counter_octet_bin = 1
                min_host_list_bin.append(tmp)
                tmp = ""

    for i in min_host_list_bin:
        min_host = min_host + str(int(i, 2)) + "."

    min_host = min_host[:-1]
    print(f"Начальный адрес хоста - {min_host}")


    '''
    Вычисление конечного адреса хоста
    '''
    max_host_bin = broadcast_full_adress_bin
    max_host_bin = max_host_bin[:-1] + "0"
    # print(max_host_bin)
    # max_host_bin = "ABCDEFGHKLMNOPQRTSWXYZ1234567890"
    # print(len(max_host_bin))
    max_host_bin_counter = 1
    max_host_bin_tmp = ""
    max_host_bin_list = []
    max_host = ""

    for i in max_host_bin:
        if max_host_bin_counter <= 8:
            max_host_bin_tmp += i
            max_host_bin_counter += 1
            if max_host_bin_counter == 9:
                max_host_bin_list.append(max_host_bin_tmp)
                max_host_bin_tmp = ""
                max_host_bin_counter = 1

    # print(max_host_bin_list)

    for i in max_host_bin_list:
        max_host = max_host + str(int(i, 2)) + "."
    max_host = max_host[:-1]
    print(f"Последний адрес хоста - {max_host}")




'''
Функция нахождения обратной маски
'''
def wildcard_calculate(mask_list):
    tmp_mask_str = ""
    tmp_wildcard_str = ""
    for i in mask_list:
        tmp_mask_str += i

    for i in tmp_mask_str:
        if i == "1":
            tmp_wildcard_str += "0"
        else:
            tmp_wildcard_str += "1"

    counter_octet = 1
    tmp_str = ""
    wildcard_bin_list = []
    wildcard_str = ""
    for i in tmp_wildcard_str:
        if counter_octet < 9:
            tmp_str += i
            counter_octet += 1
            if counter_octet == 9:
                wildcard_bin_list.append(tmp_str)
                tmp_str = ""
                counter_octet = 1

    for i in wildcard_bin_list:
        wildcard_str += str(int(i, 2)) + "."

    wildcard_str = wildcard_str[:-1]
    print(f"Wildcard - {wildcard_str}")




'''
--------------------------
ВЫЗОВЫ ФУНКЦИЙ
--------------------------
'''
apply_mask_to_ip(ip_list, mask_list)
wildcard_calculate(mask_list)
