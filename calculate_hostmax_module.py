'''
Вычисление конечного адреса хоста
'''
def calculate_hostmax(broadcast_full_adress_bin):
    max_host_bin = broadcast_full_adress_bin
    max_host_bin = max_host_bin[:-1] + "0"
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

    for i in max_host_bin_list:
        max_host = max_host + str(int(i, 2)) + "."
    max_host = max_host[:-1]
    print(f"Последний адрес хоста - {max_host}")
