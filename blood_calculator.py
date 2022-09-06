def interface():
    print("My Program")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("9 - Quit")

    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
        elif choice=='2':
            LDL_driver()

def input_HDL():
    hdl_in = input('Please enter HDL value: ')
    return int(hdl_in)

def input_LDL():
    ldl_in = input('Please enter LDL value: ')
    return int(ldl_in)

def input_total_cholesterol():
    tc_in = input('Please enter total cholesterol value: ')
    return int(tc_in)

def check_HDL(hdl_val):
    if hdl_val >= 60:
        return "Normal"
    elif 40 <= hdl_val < 60:
        return "Borderline Low"
    else:
        return "Low"

def check_LDL(ldl_val):
    if ldl_val <= 130:
        return "Normal"
    elif 130 < ldl_val < 160:
        return "Borderline High"
    elif 160 <= ldl_val < 190:
        return "High"
    else:
        return "Very High"

def HDL_driver():
    hdl_val = input_HDL()
    hdl_answer = check_HDL(hdl_val)
    output_HDL_result(hdl_val, hdl_answer)

def LDL_driver():
    ldl_val = input_LDL()
    ldl_answer = check_LDL(ldl_val)
    output_LDL_result(ldl_val, ldl_answer)

def output_HDL_result(hdl_val, charac):
    print(f"The results for an HDL value of {hdl_val} is {charac}")

def output_LDL_result(ldl_val, charac):
    print(f"The results for an LDL value of {ldl_val} is {charac}")

interface()