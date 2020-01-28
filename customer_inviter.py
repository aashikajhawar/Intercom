import math
import json
from Customer import Customer


def invite_customers(filepath, distance):
    """
    Returns list of invitable customers who are within distance kilometers from Intercom SF.

    filepath: path to a .txt file containing list of customers to check distances of
    distance: maximum distance away from Intercom SF.
    """
    #create list of all customers
    customers = []
    with open(filepath) as json_file:
        for customer in json_file.readlines():
            customer_info = json.loads(customer.strip())
            customers.append(Customer(customer_info))

    #Create list of customers within distance and sort in ascending order by user_id
    invited_customers = [customer for customer in customers if (customer.dist_to_intercom <= distance)]
    invited_customers.sort(key=lambda x: x.user_id)
    return invited_customers
