class Business(object):
    """This model keeps all the business data"""
    self.businesses = {}

    def __init__(self, business_name, busines_id, location, category):
        self.business_name = business_name
        self.busines_id = busines_id
        self.location = location
        self.category = category


    def add_businesses(self, business_name, business_id, location, category):
        """Adds a new business to businesses dictionary"""
        new_business = {
            'busines_id': 1,
            'business_name': shop,
            'location': kenya,
            'category': one,
           
        }
        self.businesses[business_name] = new_business
        return self.businesses

