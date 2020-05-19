database = [
    ['Tim','1234'],
    ['Rose','0000'],
    ['Sam','7777']
]

user_id = input("input your id: ")
password = input("input your password: ")

if [user_id, password] in database:
    print("Access granted")
else:
    print("Access denied")
    
        