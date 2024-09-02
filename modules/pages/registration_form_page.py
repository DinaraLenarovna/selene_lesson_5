from selene import have, command
from selene import browser
import paths
from modules.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.phone_number = browser.element('#userNumber')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self


    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self):
        browser.element('[for="gender-radio-2"]').click()


    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_phone_number(self, value):
        self.phone_number.type(value)
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(paths.path(file_name))

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit(self):
        browser.element('#submit').click()

    def assert_user_submitted_form(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.phone}',
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            f'{user.subjects}',
            f'{user.hobbies}',
            f'{user.photo}',
            f'{user.address}',
            f'{user.state} {user.city}'
        ))


    def register(self, user: User):
        self.open()
        self.fill_first_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_gender()
        self.fill_phone_number(user.phone)
        self.fill_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        self.fill_subjects(user.subjects)
        self.fill_hobbies()
        self.upload_picture(user.photo)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit()