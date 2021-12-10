import json
from personna import Persona

json_data = [
    {
    "first_name":"Ilyès",
    "last_name":"Fleury",
    "address_street":"Rue Paul Bert",
    "address_number":73,
    "city":"Dunkerque",
    "postcode":12681
    },{
    "first_name":"Lia",
    "last_name":"Dumont",
    "address_street":"Rue Louis-Blanqui",
    "address_number":30,
    "city":"Lille",
    "postcode":63996
    },{
    "first_name":"Eléonore",
    "last_name":"Caron",
    "address_street":"Avenue du Château",
    "address_number":87,
    "city":"Rennes",
    "postcode":78482
    },{
    "first_name":"Eva",
    "last_name":"Girard",
    "address_street":"Rue du Bon-Pasteur",
    "address_number":9,
    "city":"Rueil-Malmaison",
    "postcode":23879
    }
]

for data in json_data:
    personna=Persona(data["first_name"],data["last_name"])
    personna.set_address(address_street=data["address_street"],address_number=data["address_number"],city=data["city"],postcode=data["postcode"])
    print(personna)
    personna.show_address()
    print("--")
