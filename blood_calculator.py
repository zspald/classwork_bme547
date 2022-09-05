def interface():
    print("My Program")
    print("Options:")
    print("1 - Analyze HDL")
    print("9 - Quit")

    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()

def input_HDL():
    hdl_in = input('Please enter HDL value: ')
    return int(hdl_in)

def check_HDL(hdl_val):
    if hdl_val >= 60:
        return "Normal"
    elif 40 <= hdl_val < 60:
        return "Borderline Low"
    else:
        return "Low"

def HDL_driver():
    hdl_val = input_HDL()
    hdl_answer = check_HDL(hdl_val)
    output_HDL_result(hdl_val, hdl_answer)

def output_HDL_result(hdl_val, charac):
    print(f"The results for an HDL value of {hdl_val} is {charac}")

interface()