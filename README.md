# Intercom


### The Problem
We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our SF office for some food and drinks on us. 
Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

### The Solution
- First, I updated the JSON file to ensure proper formatting and therefore allow the data provided to be read and manipulated. 
- After reading in the file, I create a constructor class for a Customer to store all relevant data in a simple way that allows for the programs use to be expanded upon past finding invitees. 
- Within this constructor class, I used the provided formula to calculate each customer's distance from Intercom SF. 
- After all customer objects are created within the invite_customers function of customer_inviter.py, I then checked each customer's distance against the 100km limit
- Customers that were invitable, were placed in a new list which was sorted by user_id, returned, and finally print


### Running the Program
To run the program and output the desired list of customers within 100km sorted in ascending order by user_id, use the following command:  
```
~ python3 main.py 
```
### Testing
I wrote unit tests to ensure the following functionality:
- Finding customers within the correct distance 
- Sorting by user_id
- Customer constructor class is loaded with correct arguments (including conversion to radians)
- Calculation of distance to intercom

To run these tests, use the following command: 
```
~ python3 customer_tests.py 
```
