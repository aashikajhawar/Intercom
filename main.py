from customer_inviter import invite_customers

distance = 100.0 #Change this variable to alter maximum distance in kilometers
invited = invite_customers('inputs/customer.txt', distance)

print("Invite List:")
for customer in invited:
        print(customer)
