
def get_card_number(broken_card_num: str) -> str:
    start_num = int(broken_card_num.replace("*", "0"))
    end_num = int(broken_card_num.replace("*", "9"))

    mask = [2, 1] * 8
    for i in range(start_num, end_num + 10000, 10000):
        digit_sum = 0
        cur_num = list(str(i))
        for j in range(len(cur_num)):
            cur_sum = int(cur_num[j]) * mask[j]
            while cur_sum > 9:
                cur_sum = cur_sum // 10 + cur_sum % 10
            digit_sum += cur_sum
        
        if digit_sum % 10 == 0 and i % 123457 == 0:
            print(i)
            break


get_card_number("543210******1234")


