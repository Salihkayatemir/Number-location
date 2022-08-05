import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from number import number 

telephoneNumber = phonenumbers.parse(number, "C")
print(geocoder.description_for_number(telephoneNumber, "tr"))

serviceNumber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(serviceNumber, "tr"))