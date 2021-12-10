class Persona:
    def __init__(self, first_name="fname",last_name="lname"):
        self._first_name      = first_name
        self._last_name      = last_name
        self._address_street = "rue de null part"
        self._address_number = "1"
        self._city           = "Nowhere"
        self._postcode       = "00001"

    def __str__(self):
        return f"Hi ! I'm a {self._first_name} {self._last_name}"

    def set_address(self, address_street, address_number, city, postcode):
        self._address_street = address_street
        self._address_number = address_number
        self._city = city
        self._postcode = postcode

    def show_address(self):
        print(f"My full address is : {self._address_number} {self._address_street}, {self._city} ({self._postcode})")