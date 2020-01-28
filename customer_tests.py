import unittest
import math
from Customer import Customer
from customer_inviter import *

class TestInviter(unittest.TestCase):
    """
    Test Class for Customer class and customer_inviter functions.
    """

    def test_get_invited_customers(self):
        #Test for distance of 0
        self.assertEqual(invite_customers("inputs/test_customer.txt", 0), [])
        #Test for some customers being within specified distance
        self.assertEqual(len(invite_customers("inputs/test_customer.txt", 100)), 3)
        #Test for all customers being within specified distance
        self.assertEqual(len(invite_customers("inputs/test_customer.txt", 1000)), 4)

    def test_sort_invited_customers(self):
        #Test to ensure customers are sorted in order
        self.assertEqual(invite_customers("inputs/test_customer.txt", 1000)[0].user_id, 12)
        self.assertEqual(invite_customers("inputs/test_customer.txt", 1000)[3].user_id, 17)

    def test_customer_info(self):
        #Test to ensure customer args properly complete in constructor
        self.assertEqual(invite_customers("inputs/test_customer.txt", 1000)[1].user_id, 15)
        self.assertEqual(invite_customers("inputs/test_customer.txt", 1000)[1].name, "Michael Ahearn")
        self.assertEqual(invite_customers("inputs/test_customer.txt", 1000)[1].latitude, 0.6451784112922239)
        self.assertEqual(invite_customers("inputs/test_customer.txt", 1000)[1].longitude, -2.1373825618698157)
        self.assertEqual(invite_customers("inputs/test_customer.txt", 1000)[1].dist_to_intercom, 91.64741350087745)



if __name__ == "__main__":
    unittest.main()
