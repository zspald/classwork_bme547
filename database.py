def create_patient_entry(pt_first_name, pt_last_name, pt_id, pt_age):
    new_pt_dict = {}

    new_pt_dict['First Name'] = pt_first_name
    new_pt_dict['Last Name'] = pt_last_name
    new_pt_dict['Id'] = pt_id
    new_pt_dict['Age'] = pt_age
    new_pt_dict['Tests'] = []

    return new_pt_dict


def output_database(db):
    print('##### Patient Database #####')
    for pt in db:  # iterate through patients in database

        print("Name: {}, ID: {}, Age: {}, Tests: {}".format(get_full_name(db[pt]),
                                                            db[pt]['Id'],
                                                            db[pt]['Age'],
                                                            db[pt]['Tests']))
        print()  # newline


def get_full_name(pt):
    first_name = pt['First Name']
    last_name = pt['Last Name']
    full_name = first_name + ' ' + last_name
    return full_name


def find_pt(db, id):
    pt = db[id]
    return pt


def add_pt_test(db, pt_id, test_name, test_value):
    pt = find_pt(db, pt_id)
    pt['Tests'].append((test_name, test_value))


def adult_or_minor(pt):
    if pt['Age'] >= 18:
        return 'Adult'
    else:
        return 'Minor'


def main():
    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    # output_database(db)

    print(find_pt(db, 3))
    print()
    add_pt_test(db, 22, 'HDL', 140)
    output_database(db)
    add_pt_test(db, 22, 'LDL', 185)
    output_database(db)
    add_pt_test(db, 11, 'LDL', 172)
    output_database(db)

    # print("Patient {} is a {}".format(get_full_name(db[2]),
    #                                   adult_or_minor(db[2])))


if __name__ == "__main__":
    main()
