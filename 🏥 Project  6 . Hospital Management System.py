# ------------------------------------------
# Hospital Data
# ------------------------------------------

patients = []
doctors = []
appointments = []
treatments = []
medicines = []

# ------------------------------------------
# Patient Registration
# ------------------------------------------

def patient_registration():
    patient_name = input("enter patient name: ")
    patient_age = input("enter patient age: ")
    
    patients.append({ patient_name : patient_age })

    print("Patient registered successfully")



# ------------------------------------------
# Doctor List
# ------------------------------------------
doctors = []


def doctor_list():

    doctor_name= input("enter doctor name: ")
    
    doctors.append(doctor_name)
    
    print(" doctor added successfully")


# ------------------------------------------
# Appointment Booking
# ------------------------------------------

def appointment_booking():

        patient_name = input("enter patient name: ")

        doctor_name= input("enter doctor name: ")

        appointments.append({ patient_name : doctor_name })

        print( "booking successful message")


# ------------------------------------------
# Patient Search
# ------------------------------------------

def patient_search():

    patient_name = input("enter patient name: ")

    for patient in patients:

        if patient_name in patient:
            print("Patient found")
            print("Name:", patient_name)
            print("Age:", patient[patient_name])
            break

    else:
        print("Patient not found")


# ------------------------------------------
# Treatment Details
# ------------------------------------------

def treatment_details():

    patient_name = input("enter patient name: ")
    treatment_name = input("enter treatment name: ")

    treatments.append({patient_name: treatment_name})

    print("Treatment added successfully")


# ------------------------------------------
# Medicine Charges
# ------------------------------------------

def medicine_charges():

    patient_name = input("enter patient name: ")
    medicine_name = input("enter medicine name: ")
    medicine_price = float(input("enter medicine price: "))

    medicines.append({
        patient_name: {
            "medicine": medicine_name,
            "price": medicine_price
        }
    })

    print("Medicine charges added successfully")

# ------------------------------------------
# Total Bill
# ------------------------------------------

def total_bill():

    patient_name = input("enter patient name: ")

    treatment_charges = float(input("enter treatment charges: "))
    medicine_charges = float(input("enter medicine charges: "))

    total = treatment_charges + medicine_charges

    print("Total bill:", total)

# ------------------------------------------
# Discharge
# ------------------------------------------

def discharge():

    patient_name = input("enter patient name: ")

    for patient in patients:

        if patient_name in patient:

            patients.remove(patient)

            print("Patient discharged successfully")

            break

    else:

        print("Patient not found")

# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Patient Registration")
    print("2. Doctor List")
    print("3. Appointment Booking")
    print("4. Patient Search")
    print("5. Treatment Details")
    print("6. Medicine Charges")
    print("7. Total Bill")
    print("8. Discharge")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        patient_registration()

    elif choice == "2":
        doctor_list()

    elif choice == "3":
        appointment_booking()

    elif choice == "4":
        patient_search()

    elif choice == "5":
        treatment_details()

    elif choice == "6":
        medicine_charges()

    elif choice == "7":
        total_bill()

    elif choice == "8":
        discharge()

    elif choice == "9":
        print("Thank you for using Hospital Management System!")
        break

    else:
        print("Invalid choice")
