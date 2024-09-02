from modules.pages.registration_form_page import RegistrationPage
from modules.users import User


def test_student_registration_form():
    form_action = RegistrationPage()
    person = User(name='Dinara',
                       last_name='Safina',
                       email='dinatest@bk.ru',
                       gender='Female',
                       phone='7999991919',
                       day_of_birth='11',
                       month_of_birth='April',
                       year_of_birth='1999',
                       subjects='Maths',
                       photo='test_image.jpg',
                       hobbies='Sports, Reading',
                       address='Russia, Ufa, Lenina St., 1',
                       state='Haryana',
                       city='Panipat')

    form_action.open()
    form_action.register(person)
    form_action.assert_user_submitted_form(person)


