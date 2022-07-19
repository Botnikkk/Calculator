import math

def check_var(calculation) :
    string = calculation
    for variable in ["+", "-", "x", "/" ] :
        check = str(string).split(variable) 
        string = ""
        for i in check :
            try :
                int(i)
                check = check.remove(i)             
            except :
                string += i
                continue
                
def try_sum(num_str) :
    sum = 0 
    output_list = []
    for i in num_str :
        num_list = str(i).split("+")
        for i in num_list : 
            i = str(i).strip()
            try :
                a = int(i) 
                sum += a 
            except :
                if "-" not in i and "x" in i :
                    mul_output = try_mul(i)
                    sum += mul_output
                elif "x" and "-" not in i :
                    div_output=  try_div(i)
                    sum += div_output
                else:  
                    output_list.append(i)
                    continue 
    return [sum, output_list]

def try_sub(num_str) :
    final_sub = 0
    num_list = []
    sub_list = []
    for i in num_str : 
        num_list = str(i).split("-")     
        try :
            sub = int(num_list[0])
            for i in num_list[1:len(num_list)+1] : 
                i = str(i).strip()
                try :
                    sub -= int(i)
                except :
                    if "x" not in i :
                        div_output=  try_div(i)
                        sub -= div_output
                    else:  
                        mul_output = try_mul(i)
                        sub -= mul_output
                        continue
            sub_list.append(int(sub))
            
        except : 
            if "x" not in i :
                div_output=  try_div(num_list[0])
                sub = div_output
            else:  
                mul_output = try_mul(num_list[0])
                sub = mul_output
            for i in num_list[1:len(num_list)+1] : 
                i = str(i).strip()
                try :       
                    sub -= int(i)
                except :
                    if "x" not in i :
                        div_output=  try_div(i)
                        sub -= div_output
                    else:  
                        mul_output = try_mul(i)
                        sub -= mul_output
                        continue
            sub_list.append(int(sub))
    final_sub = sum(sub_list)
    return int(final_sub)

def try_mul(num_str) :
    final_mul = 0
    mul_list = []
    mul = 1
    num_list = str(num_str).split("x")
    for i in num_list :
        i = str(i).strip()
        if "/" in  i :
            div_output = try_div(i)
            if div_output == 0 :
                div_output = 1

            mul = div_output
        else:     
            mul = int(i)           
        mul_list.append(mul)
    final_mul = math.prod(mul_list)
    return int(final_mul)

def try_div(num_str) :
    final_div=0
    num_list = str(num_str).split("/")
    if len(num_list) > 1 :
        final_div = int(num_list[0].strip())
        for i in num_list[1:] : 
                i = str(i).strip()
                try :
                    final_div /= int(i)
                except :
                    continue        
    return float(final_div)

def calc(calculation) :  
    sum_output = try_sum([calculation])
    sub_output = try_sub(sum_output[1])
    ans = int(sum_output[0]) + sub_output
    print(ans)

calculation = input("Enter the calculation you want to perform\n- ")  
while calculation.lower() != 'end' :
    calc(calculation)
    calculation = input("Enter the calculation you want to perform\n- ")  

