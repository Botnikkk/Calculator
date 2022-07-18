import math

def try_sum(num_str) :
    sum = 0 
    output_list = []
    for i in num_str :
        num_list = str(i).split("+")
        if len(num_list) > 1 :
            for i in num_list : 
                try :
                    a = int(i) 
                    sum += a 
                except :
                    output_list.append(i)
                    continue 
        else  :
            continue
    return [sum, output_list]

def try_sub(num_str) :
    final_sub = 0
    next_check_output_list = []
    num_list = []
    sub_list = []
    for i in num_str : 
        num_list = str(i).split("-")
        if len(num_list) > 1 :
            if "x" in num_list[0] :
                a = int(num_list[0][0])
                b = num_list[0][1:]
                new_str= str(a*-1) + b
                num_list[0] = new_str
                
            try :
                sub = int(num_list[0])
                for i in num_list[1:len(num_list)+1] : 
                    try :
                        a = int(i)
                        sub -= a
                    except :
                        next_check_output_list.append(i)
                        continue
                sub_list.append(int(sub))
                final_sub = sum(sub_list)
                
            except : 
                sub = 0
                for i in num_list : 
                    try :
                        a = int(i)
                        sub -= a
                    except :
                        next_check_output_list.append(i)
                        continue
                sub_list.append(int(sub))
                final_sub = sum(sub_list)
        else  :
            continue
    return [int(final_sub), next_check_output_list]

def try_mul(num_str) :
    final_mul = 0
    next_check_output_list = []
    num_list = []
    mul_list = []
    for i in num_str : 
        if "-" not in i[1:] :
            mul = 1
            num_list = str(i).split("x")
            if len(num_list) > 1 :
                for i in num_list : 
                        try :
                            a = int(i)
                            mul *= a
                        except :
                            num_list.remove(i)
                            next_check_output_list.append(i)
                            continue             
                mul_list.append(mul)
                final_mul = math.prod(mul_list)
            else : 
                next_check_output_list.append(i)
                continue
    print(final_mul)
    return [final_mul, next_check_output_list]

def try_div(num_str) :
    final_mul = 0
    next_check_output_list = []
    num_list = []
    mul_list = []
    for i in num_str : 
        if "-" not in i[1:] :
            mul = 1
            num_list = str(i).split("x")
            if len(num_list) > 1 :
                for i in num_list : 
                        try :
                            a = int(i)
                            mul *= a
                        except :
                            num_list.remove(i)
                            next_check_output_list.append(i)
                            continue             
                mul_list.append(mul)
                final_mul = math.prod(mul_list)
            else : 
                next_check_output_list.append(i)
                continue
    print(final_mul)
    return [final_mul, next_check_output_list]

calculation = input("Enter the calculation you want to perform\n- ")

def calc() : 
    sum_output = try_sum([calculation])
    sub_output = try_sub(sum_output[1])
    mult_output_by_sum = try_mul(sum_output[1])
    mult_output_by_sub = try_mul(sub_output[1])

    print(int(sum_output[0]) + sub_output[0] + mult_output_by_sum[0] - mult_output_by_sub[0])



calc()
