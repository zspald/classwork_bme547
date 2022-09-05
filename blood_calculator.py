def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")

    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return

def input_HDL():
    hdl_in = input('Please enter HDL value: ')
    return int(hdl_in)

def check_HDL(hdl_val):
    if hdl_val >= 60:
        return "Normal"
    elif hdl_val < 60 and hdl_val >= 40:
        return "Borderline Low"
    elif hdl_val < 40:
        return "Low"

interface()