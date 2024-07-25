'''
Вычисление начального адреса хоста
'''
def calculate_hostmin(full_network_adress_bin):
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
