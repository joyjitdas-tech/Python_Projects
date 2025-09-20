#Blood Donation
class Donor:
    def __init__(self,name,blood_type,contact_info,location):
        self.name = name
        self.blood_type = blood_type
        self.contact_info = contact_info
        self.location = location

#blood_donation register system
class blood_donation_system:
    def __init__(self):
        self.donors = []
    #new donor registar
    def register_donor(self,name,blood_type,contact_info,location):
        new_donor = Donor(name,blood_type,contact_info,location)
        self.donors.append(new_donor)
        print(f"Donor {name} registered successfully!")

    #Method to find matching donor
    def search_donor(self, blood_type, location=None):
        donor_match = [
        donor for donor in self.donors
        if donor.blood_type == blood_type and (location is None or donor.location == location)
    ]
    
        if donor_match:
            for donor in donor_match:
                print(f"Donor found: {donor.name}, Location: {donor.location}, Contact: {donor.contact_info}")
        else:
            print(" No donor found with given criteria.")

        
#main function
def main():
    blood_bank = blood_donation_system()

    while True:
        print("\nwelcome to the Blood Donation System")
        print("1. Register as Donor")
        print("2. Search for a Donor")
        print("3. Exit")


        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Enter the details of Donor.")
            name = input("Enter name: ")
            blood_type = input("Enter your Blood type: ")
            contact_info = input("Enter contact information: ")
            location = input("Enter Location: ")
            blood_bank.register_donor(name,blood_type,contact_info,location)
        
        elif choice == "2":
            blood_type = input("Enter your require Blood type: ")
            location = input("Enter Location: ")
            blood_bank.search_donor(blood_type,location)
        elif choice == "3":
            print("Thank you for using Blood Donation system")
            break

        else:
            print("Invaild operation")
if __name__ == "__main__":
    main()