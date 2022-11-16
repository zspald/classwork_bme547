import tkinter as tk
from tkinter import ttk, filedialog
import db_client
from PIL import Image, ImageTk


def create_blood_type(letter, rh):
    output = f'{letter}{rh}'
    return output


def upload_to_server(patient_name, patient_id, patient_blood_letter,
                     patient_rh):
    blood_type = create_blood_type(patient_blood_letter, patient_rh)
    msg, code = db_client.upload_patient_info(patient_name, patient_id,
                                              blood_type)
    return msg, code


def main_window():

    def get_update_info():
        print('Get data')
        root.after(2000, get_update_info)

    def ok_cmd():
        # get data from interface
        if rh_button.get() == "":
            print('Choose a rh factor')
            return
        patient_name = patient_name_entry.get()
        patient_id = patient_id_entry.get()
        patient_blood_letter = blood_letter_selection.get()
        patient_rh = rh_button.get()

        # call other testable functions to do the work
        patient_id = int(patient_id)
        msg, code = upload_to_server(patient_name, patient_id,
                                     patient_blood_letter,
                                     patient_rh)

        # update GUI based on results of other functions
        status_label.configure(text=msg)

    def cancel_cmd():
        root.destroy()

    def picture_cmd():
        # new_file = "q2_entorhinal_cortex.jpg"
        new_file = filedialog.askopenfilename()
        if new_file == '':
            return
        print(f'Filename: {new_file}')
        pil_image = Image.open(new_file)
        x_size, y_size = pil_image.size
        new_y = 200
        new_x = int((new_y / y_size) * x_size)
        pil_image = pil_image.resize((new_x, new_y))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

    root = tk.Tk()
    root.title('Blood Donor Database Window')
    root.geometry("700x400")

    ttk.Label(root, text='Blood Donor Database').grid(column=0, row=0,
                                                      columnspan=2, sticky='W')

    ttk.Label(root, text='Name: ').grid(column=0, row=1, sticky='E')
    patient_name_entry = tk.StringVar()
    ttk.Entry(root, width=25, textvariable=patient_name_entry).grid(column=1,
                                                                    row=1)

    ttk.Label(root, text='ID: ').grid(column=0, row=2, sticky='E')
    patient_id_entry = tk.IntVar()
    patient_id_entry.set('')
    ttk.Entry(root, width=25, textvariable=patient_id_entry)\
        .grid(column=1, row=2)

    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text='A', variable=blood_letter_selection,
                    value='A')\
        .grid(column=0, row=3, sticky='W')
    ttk.Radiobutton(root, text='B', variable=blood_letter_selection,
                    value='B')\
        .grid(column=0, row=4, sticky='W')
    ttk.Radiobutton(root, text='AB', variable=blood_letter_selection,
                    value='AB')\
        .grid(column=0, row=5, sticky='W')
    ttk.Radiobutton(root, text='O', variable=blood_letter_selection,
                    value='O')\
        .grid(column=0, row=6, sticky='W')

    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text='Rh Positive', variable=rh_button, onvalue='+',
                    offvalue='-')\
        .grid(column=1, row=4)

    ttk.Label(root, text='Closest Donation Center: ').grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_combo.grid(column=2, row=1)
    donor_combo['values'] = ['Durham', 'Cary', 'Raleigh', 'Chapel Hill']
    donor_combo.state(['readonly'])

    ttk.Button(root, text='Ok', command=ok_cmd).grid(column=1, row=6)
    ttk.Button(root, text='Cancel', command=cancel_cmd).grid(column=2, row=6)

    picture_button = ttk.Button(root, text='Load Picture', command=picture_cmd)
    picture_button.grid(column=2, row=8)

    status_label = ttk.Label(root, text='Status: ')
    status_label.grid(column=0, row=8)

    pil_image = Image.open('IMG-0421.JPG')
    pil_image = pil_image.resize((300, 200))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=1, row=8)

    root.after(2000, get_update_info)
    root.mainloop()


if __name__ == '__main__':
    main_window()
