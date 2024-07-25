from convert_data_to_binary_module import data_to_binary
from wildcard_calculate_module import wildcard_calculate
from  calculate_hostmin_module import calculate_hostmin
from  calculate_hostmax_module import calculate_hostmax
from calculate_broadcast_address_module import calculate_broadcast_address

print("Программа показывающая подсеть по маске")
print("---------------------------------------")
ip = input("Введите IP адресс: ")
mask = input("Введите маску: ")


ip_list = data_to_binary(ip)
mask_list = data_to_binary(mask)

'''
Функция наложения маски на IP и вычисления
'''
def apply_mask_to_ip(ip, mask):
    counter_bit_mask = 0
    ip_bin_str = ""

    for oct_mask in mask:
        for bit_mask in oct_mask:
            if bit_mask == "1":
                counter_bit_mask += 1

    for oct_ip in ip:
        for bit_ip in oct_ip:
            ip_bin_str += bit_ip

    print()
    network_adress_part = ip_bin_str[:counter_bit_mask]
    host_adress_binary_part = ip_bin_str[counter_bit_mask:len(ip_bin_str)]

    full_network_adress_bin = network_adress_part
    for i in range(0, 32 - len(network_adress_part)):
        full_network_adress_bin += "0"

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

    revrs_host = host_adress_binary_part[::-1]
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

    # return full_network_adress_bin

    calculate_broadcast_address(full_network_adress_bin, counter_bit_mask)
    broadcast_full_adress_bin = calculate_broadcast_address(full_network_adress_bin, counter_bit_mask)
    # '''
    # вычисление broadcast адреса
    # '''
    # network_adress_part_bin = full_network_adress_bin[:counter_bit_mask]
    #
    # for i in range(0, 32 - counter_bit_mask):
    #     network_adress_part_bin += "1"
    #
    # broadcast_full_adress_bin = network_adress_part_bin
    #
    # counter_broadcast_octet = 0
    # broadcast_full_adress_list = []
    # tmp = ""
    #
    # for i in broadcast_full_adress_bin:
    #     counter_broadcast_octet += 1
    #     if counter_broadcast_octet <= 8:
    #         tmp += i
    #         if counter_broadcast_octet == 8:
    #             broadcast_full_adress_list.append(tmp)
    #             tmp = ""
    #             counter_broadcast_octet = 0
    #
    # broadcast_adress = ""
    #
    # for i in broadcast_full_adress_list:
    #     broadcast_adress = broadcast_adress + str(int(i, 2)) + "."
    # broadcast_adress = broadcast_adress[:-1]
    # print(f"Широковещятельный адрес - {broadcast_adress}")


    '''
    Вызов модуля вычисления начального адреса хоста
    '''
    calculate_hostmin(full_network_adress_bin)

    '''
    Вызов модуля вычисления конечного адреса хоста
    '''
    calculate_hostmax(broadcast_full_adress_bin)




'''
--------------------------
ВЫЗОВЫ ФУНКЦИЙ
--------------------------
'''
apply_mask_to_ip(ip_list, mask_list)
wildcard_calculate(mask_list)
