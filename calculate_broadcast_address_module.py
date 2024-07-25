'''
вычисление broadcast адреса
'''
def calculate_broadcast_address(full_network_adress_bin, counter_bit_mask):
    network_adress_part_bin = full_network_adress_bin[:counter_bit_mask]

    for i in range(0, 32 - counter_bit_mask):
        network_adress_part_bin += "1"

    broadcast_full_adress_bin = network_adress_part_bin

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

    broadcast_adress = ""

    for i in broadcast_full_adress_list:
        broadcast_adress = broadcast_adress + str(int(i, 2)) + "."
    broadcast_adress = broadcast_adress[:-1]
    print(f"Широковещятельный адрес - {broadcast_adress}")

    return broadcast_full_adress_bin
