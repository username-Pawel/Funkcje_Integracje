from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone_private, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_private = phone_private
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_private} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name) + 1  # +1 for the space between names



class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone_private, email, position, company, phone_work):
        super().__init__(first_name, last_name, phone_private, email)
        self.position = position
        self.company = company
        self.phone_work = phone_work

    def contact(self):
        print(f"Wybieram numer {self.phone_work} i dzwonię do {self.first_name} {self.last_name}")


def create_contacts(contact_type, quantity):
     contacts = []
     for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_private = fake.phone_number()
        email = fake.email()
        
        if contact_type == "business":
            position = fake.job()
            company = fake.company()
            phone_work = fake.phone_number()
            contact = BusinessContact(first_name, last_name, phone_private, email, position, company, phone_work)
        else:
            contact = BaseContact(first_name, last_name, phone_private, email)
        
        contacts.append(contact)
        
        return contacts


def show_contacts(contacts):
    for contact in contacts:
        print(f"{contact.first_name} {contact.last_name}, Email: {contact.email}, Label length: {contact.label_length}")
        contact.contact()


if __name__ == "__main__":
    base_contacts = create_contacts("base", 3)       
    business_contacts = create_contacts("business", 2)  
    
    print("Base Contacts:")
    show_contacts(base_contacts)
    
    print("\nBusiness Contacts:")
    show_contacts(business_contacts)
