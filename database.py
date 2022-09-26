class Patient:

    def __init__(self, first_name, last_name, id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.patient_id = id
        self.age = age
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(pt_first_name, pt_last_name, pt_id, pt_age):
    new_pt = Patient(pt_first_name, pt_last_name, pt_id, pt_age)

    # new_pt = {}
    # new_pt['First Name'] = pt_first_name
    # new_pt['Last Name'] = pt_last_name
    # new_pt['Id'] = pt_id
    # new_pt['Age'] = pt_age
    # new_pt['Tests'] = []

    return new_pt


def output_database(db):
    print('##### Patient Database #####')
    for pt in db.values():  # iterate through patients in database

        print("Name: {}, ID: {}, Age: {}, Tests: {}".format(get_full_name(pt),
                                                            pt['Id'],
                                                            pt['Age'],
                                                            pt['Tests']))
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
    x = Patient("David", "Ward", "", "")
    print(x.full_name())

    y = Patient("Edward", "Smith", "", "")
    print(y.full_name())
    # print(type(x))
    exit()

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
