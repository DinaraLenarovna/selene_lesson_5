from selene import browser, be, have
import os


def test_filling_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Dinara')
    browser.element('#lastName').should(be.blank).type('Safina')
    browser.element('#userEmail').should(be.blank).type('dinatest@bk.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('9999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('[value="1999"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('[value="3"]').click()
    browser.element('.react-datepicker__day--011').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_image.jpg'))
    browser.element('#currentAddress').type('Russia, Ufa, Lenina St., 1')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Dinara Safina', 'dinatest@bk.ru', 'Female', '9999999999', '11 April,1999', 'Maths', 'Sports, Reading',
        'test_image.jpg', 'Russia, Ufa, Lenina St., 1', 'Haryana Panipat'
    ))
