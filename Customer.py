import math

""" Define Global Variables """
INTERCOM_LAT = 37.788802 * math.pi/180 #converted to radians
INTERCOM_LONG = -122.4025067 * math.pi/180 #converted to radians
EARTH_RADIUS = 6371.0

class Customer:
    def __init__(self, customer_info):
        """
        Stores all necessary customer details.

        latitude: latitude location data for customer converted to radians
        user_id: id number of customer
        name: name of customer
        longitude: longitudine location data for customer converted to radians
        dist_to_intercom: great-circle distance between customer and Intercom SF
        """
        self.latitude = self.degree_to_radian(float(customer_info['latitude']))
        self.user_id = customer_info['user_id']
        self.name = customer_info['name']
        self.longitude = self.degree_to_radian(float(customer_info['longitude']))
        self.dist_to_intercom = self.dist_to_intercom()

    def __str__(self):
        return f"{self.user_id}: {self.name}"

    def degree_to_radian(self, degrees):
        return degrees * math.pi/180

    def dist_to_intercom(self):
        """ Returns a customer's distance to the Intercom SF office using great-circle distance. """
        central_angle = math.acos(math.sin(INTERCOM_LAT) * math.sin(self.latitude) +
                             (math.cos(INTERCOM_LAT) * math.cos(self.latitude) * math.cos(INTERCOM_LONG - self.longitude)))
        return EARTH_RADIUS * central_angle
