from modules.pages.registration_form_page import RegistrationPage


def test_filling_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name('Dinara')
    registration_page.fill_last_name('Safina')
    registration_page.fill_email('dinatest@bk.ru')
    registration_page.choose_gender()
    registration_page.fill_phone_number('9999999999')
    registration_page.fill_date_of_birth('1999', 'April', '11')
    registration_page.fill_subjects('Maths')
    registration_page.fill_hobbies()
    registration_page.upload_picture('test_image.jpg')
    registration_page.fill_address('Russia, Ufa, Lenina St., 1')
    registration_page.select_state('Haryana')
    registration_page.select_city('Panipat')
    registration_page.submit()

    registration_page.assert_user_submitted_form('Dinara Safina', 'dinatest@bk.ru', 'Female', '9999999999', '11 April,1999', 'Maths', 'Sports, Reading',
        'test_image.jpg', 'Russia, Ufa, Lenina St., 1', 'Haryana Panipat')

