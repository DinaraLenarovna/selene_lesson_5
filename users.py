

class User:
    name = str
    last_name = str
    email = str
    gender = str
    phone = str
    day_of_birth = str
    month_of_birth = str
    year_of_birth = str
    subjects = str
    hobbies = str
    address = str
    state = str
    city = str
    state_and_city = str
    name_and_last_name = str
    photo = str
    date_of_birth = str

    def __init__(self, name, last_name, email, gender,
                 phone, day_of_birth, month_of_birth, year_of_birth,
                 subjects, hobbies, address, state, city, photo):
        self.subjects = subjects
        self.address = address
        self.state = state
        self.hobbies = hobbies
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.city = city
        self.name = name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.phone = phone
        self.photo = photo
