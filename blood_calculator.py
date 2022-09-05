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

   
interface()