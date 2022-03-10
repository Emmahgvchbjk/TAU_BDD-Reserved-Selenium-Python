import random
import string

class CreateStrings():

    def generate_string(lenght):
        my_string = ''.join(random.choice(string.ascii_lowercase) for i in range(lenght))
        return my_string

    def generate_mail(lenght):
        adress = ''.join(random.choice(string.ascii_lowercase) for i in range(lenght))
        domain = ''.join(random.choice(string.ascii_lowercase) for i in range(lenght-3))
        return adress+"@"+domain+".com"

print(CreateStrings.generate_string(6))
print(CreateStrings.generate_mail(6))

