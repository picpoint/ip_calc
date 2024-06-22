print("Программа показывающая подсеть по маске")
print("---------------------------------------")
ip = input("Введите IP адресс: ")
# mask = input("Введите маску: ")

print(ip)
# print(mask)

ip_list = ip.split(".")
print(ip_list)

ip_list_bin = []

for oct in ip_list:
    oct = int(oct)
    ip_list_bin.append(bin(oct)[2:])

print(ip_list_bin)

for bin_oct in ip_list_bin:
    if len(bin_oct) < 8:
        print(len(bin_oct))