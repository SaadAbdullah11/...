import phonenumbers
number="+923212114345"

from phonenumbers import geocoder
c_number=phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(c_number,"en"))

from phonenumbers import carrier
service_number=phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

