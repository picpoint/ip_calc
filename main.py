# print("Программа показывающая подсеть по маске")
# print("---------------------------------------")
# ip = input("Введите IP адресс: ")
# mask = input("Введите маску: ")
#
# '''
# Функция перевода IP в двоичный формат
# '''
# def ip_to_binary(ip):
#     ip_list_bin = []
#     res_lst = []
#     ip_list = ip.split(".")
#
#     for oct in ip_list:
#         oct = int(oct)
#         ip_list_bin.append(bin(oct)[2:])
#
#     for i in ip_list_bin:
#         if len(i) < 8:
#             lngth = 8 - len(i)
#             while lngth != 0:
#                 i = "0" + i
#                 lngth -=1
#             res_lst.append(i)
#         else:
#             res_lst.append(i)
#
#     return res_lst
#
#
# '''
# Функция перевода маски в двоичный формат
# '''
# def mask_to_binary(mask):
#     mask_list = mask.split(".")
#     mask_list_binary = []
#     res_mask_list_binary = []
#
#     for i in mask_list:
#         oct = bin(int(i))
#         mask_list_binary.append(oct[2:])
#
#     for oct in mask_list_binary:
#         while len(oct) < 8:
#             oct = "0" + oct
#         res_mask_list_binary.append(oct)
#     return res_mask_list_binary
#
#
# ip_list = ip_to_binary(ip)
# mask_list = mask_to_binary(mask)
#
#
# '''
# Функция наложения маски на IP и вычисления
# '''
# def apply_mask_to_ip(ip, mask):
#     # print(ip)
#     # print(mask)
#     counter_bit_mask = 0
#     ip_bin_str = ""
#     network_ip = ""
#     host_ip = ""
#
#     for oct_mask in mask:
#         for bit_mask in oct_mask:
#             # print(bit_mask)
#             if bit_mask == "1":
#                 counter_bit_mask += 1
#     # print(counter_bit_mask)
#
#     for oct_ip in ip:
#         for bit_ip in oct_ip:
#             ip_bin_str += bit_ip
#
#
#     print()
#     # print(f"IP в строке - {ip_bin_str}")
#     print(f"Длинна маски {counter_bit_mask}")
#     network_adress_part = ip_bin_str[:counter_bit_mask]
#     # print(f"Network Adress - {network_adress_part}")
#     host_adress_binary_part = ip_bin_str[counter_bit_mask:len(ip_bin_str)]
#     print(f"Host adress - {host_adress_binary_part}")
#
#     full_network_adress_bin = network_adress_part
#     for i in range(0, 32 - len(network_adress_part)):
#         full_network_adress_bin += "0"
#
#     # print(f"Full NA - {full_network_adress_bin}")
#     full_network_adress_bin_list = []
#     counter = 0
#     tmp = ""
#     network_adress = ""
#
#     for i in full_network_adress_bin:
#         tmp += i
#         counter += 1
#         if counter == 8:
#             full_network_adress_bin_list.append(tmp)
#             counter = 0
#             tmp = ""
#
#     for i in full_network_adress_bin_list:
#         octet = int(i, 2)
#         network_adress = network_adress + str(octet) + "."
#
#     network_adress = network_adress[:-1]
#     print(f"Адрес сети - {network_adress}")
#
#
#
#
#
#
#
#
#     # hosts_in_network = 2 ** (len(host_adress_binary_part)) - 2
#     # print(f"Количество хостов в сети - {hosts_in_network}")
#
#
#
#
#
#
#
#
#
# apply_mask_to_ip(ip_list, mask_list)


host = "0000000001111011"

print(host)

res = host[::-1]
print(res)