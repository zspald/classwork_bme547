"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""

# gets input for desired diagnosis from user
def diagnosis_input():
    # print information for user choice
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")

    # request user input from choices
    diagnosis = int(input("Enter a number: "))

    return diagnosis

# gets input for user weight in kg
def weight_input():
    # print information for user choice
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")

    # request input from user
    weight_input = input("Enter weight: ")
    weight_data = weight_input.split(" ")

    # determine weight units
    weight = float(weight_data[0])
    units = weight_data[1]

    # convert to kg if necessary
    if units == "lb":
        weight = weight / 2.205

    return weight

# gets the proper mg per kg conversion factor for a given diagnosis
def get_dosage_conv_factor(diagnosis):
    # use diagnosis choice to select proper mg per kg conversion factor
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]

    return dosage_mg_per_kg

# outputs calculated dosage information for given weight and conversion factor
def output_dosage_info(weight, dosage_mg):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg))

# calculate dosage amount
def dose_amount(diagnosis, weight):
    return weight * get_dosage_conv_factor(diagnosis)

# runs dosage pipeline to receiver user input and output dosage information
def dose_driver():
    # get diagnosis from user
    diagnosis = diagnosis_input()

    # get weight from user
    weight = weight_input()

    # calculate dosage amount for first day
    dosage_mg_first_day = dose_amount(diagnosis, weight)

    # display dosage info to user
    output_dosage_info(weight, dosage_mg_first_day)


if __name__ == '__main__':
    dose_driver()