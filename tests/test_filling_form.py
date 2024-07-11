from selene import browser, be, have


def test_page():
    browser.open('/')
    browser.element('[class="text-center"]').should(have.text('Practice Form'))


def test_filling_form():
    browser.element('#firstName').should(be.blank).type('Dinara')
    browser.element('#lastName').should(be.blank).type('Safina')
    browser.element('#email').should(be.blank).type('dinatest@bk.ru')
    browser.element('#gender-radio-2').should(be.enabled)
    browser.element('#userNumber').should(be.blank).type('+79999999999')



