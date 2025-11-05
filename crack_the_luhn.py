

def get_card_number(broken_card_num: str) -> str:
    symbols_list = list(broken_card_num)
    stars_idx = [i for i in range(len(symbols_list)) if symbols_list[i] == "*"]
    mask = [2, 1] * 8
    mask_nums = [mask[i] for i in range(len(mask)) if i in stars_idx]
    symbols_list = [int(s) for s in symbols_list if s != "*"]
    digits_sum = sum(symbols_list)
    num = 1
    pos = 0
    prev_num = 0
    while digits_sum % 10:
        temp_sum = digits_sum

        curr_arr = []
        for i in range(len(mask_nums)):
            
            if i == pos:
                curr_num = mask_nums[i] * num
                print(curr_num)
                while curr_num > 9:
                    curr_num = curr_num // 10 + curr_num % 10
                
                temp_sum += curr_num
                curr_arr.append(num)
            else:
                curr_num = mask_nums[i] * prev_num
                while curr_num > 9:
                    curr_num = curr_num // 10 + curr_num % 10
                temp_sum += curr_num
                curr_arr.append(prev_num)
            
            if temp_sum % 10 == 0:
                digits_sum = temp_sum
                print(curr_arr)
                break
        print(curr_arr)
        if digits_sum % 10 == 0:
            break




        pos += 1
        print(pos)
        if pos == len(mask_nums):
            pos = 0
            prev_num = num
            num += 1
            





print(get_card_number("543210******1234"))


