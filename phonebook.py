contacts={}

def add_contact():
    name=input('Enter Name: ').strip()
    if name in contacts:
        print('This name is exited')
        return
    phone=input('Enter the number: ').strip()
    email=input('Enter Email: ').strip()
    
    contacts[name]={'phone': phone, 'Email': email if email else 'N/A'}
    print('ok name saved successfully' )

add_contact()