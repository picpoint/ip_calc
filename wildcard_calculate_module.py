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

