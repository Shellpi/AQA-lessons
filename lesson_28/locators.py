"""Файл с локаторами для всех страниц."""

from selenium.webdriver.common.by import By

# Локаторы для HomePage
HOME_PAGE_LOCATORS = {
    'guest_log_in_button': (By.XPATH, "//button[@class = 'header-link -guest']"),
    'menu_dropdown_button': (By.ID, 'userNavDropdown'),
    'sign_in_button': (By.XPATH, "//button[@class='btn btn-outline-white header_signin']"),
    'sign_up_button': (By.XPATH, "//button[@class = 'hero-descriptor_btn btn btn-primary']"),
}

# Локаторы для GaragePage
GARAGE_PAGE_LOCATORS = {
    'menu_log_out_button': (By.XPATH, "//a[@class='btn btn-link text-danger btn-sidebar sidebar_btn']"),
    'dropdown_log_out_button': (By.XPATH, "//button[@class = 'dropdown-item btn btn-link user-nav_link']"),
}

# Локаторы для SignIn
SIGN_IN_LOCATORS = {
    'sign_in_button': (By.XPATH, "//button[@class='btn btn-outline-white header_signin']"),
    'registration_login_button': (By.XPATH, "//button[@class='btn btn-link'][text()='Registration']"),
    'email_textfield': (By.ID, "signinEmail"),
    'password_textfield': (By.ID, "signinPassword"),
    'login_button': (By.XPATH, "//button[@class='btn btn-primary']")
}

# Локаторы для SignUp
SIGN_UP_LOCATORS = {
    'name': (By.ID, "signupName"),
    'last_name': (By.ID, "signupLastName"),
    'email': (By.ID, "signupEmail"),
    'password': (By.ID, "signupPassword"),
    'confirm': (By.ID, "signupRepeatPassword"),
    'register_button': (By.XPATH, '//button[text()="Register"]'),
    'success_message': (By.XPATH, '//p[text()="Registration complete"]'),
}

# Локаторы для ошибок в SignUp
SIGN_UP_ERROR_LOCATORS = {
    'Name required': (By.XPATH, '//p[text()="Name required"]'),
    'Name has to be from 2 to 20 characters long': (By.XPATH, '//p[text()="Name has to be from 2 to 20 characters long"]'),
    'Last name required': (By.XPATH, '//p[text()="Last name required"]'),
    'Last name has to be from 2 to 20 characters long': (By.XPATH, '//p[text()="Last name has to be from 2 to 20 characters long"]'),
    'Email required': (By.XPATH, '//p[text()="Email required"]'),
    'Email is incorrect': (By.XPATH, '//p[text()="Email is incorrect"]'),
    'Password required': (By.XPATH, '//p[text()="Password required"]'),
    'Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter': (
        By.XPATH, '//p[contains(text(), "Password has to be from 8 to 15 characters long")]'),
    'Re-enter password required': (By.XPATH, '//p[text()="Re-enter password required"]'),
    'Passwords do not match': (By.XPATH, '//p[text()="Passwords do not match"]'),
}

# Локаторы для ошибок в SignIn
SIGN_IN_ERROR_LOCATORS = {
    'Email required': (By.XPATH, '//p[text()="Email required"]'),
    'Email is incorrect': (By.XPATH, '//p[text()="Email is incorrect"]'),
    'Password required': (By.XPATH, '//p[text()="Password required"]'),
    'Wrong email or password': (By.XPATH, '//p[@class="alert alert-danger"]')
}

SIGN_IN_SUCCESS_LOCATORS = {
    'login_success_message': (By.XPATH, '//p[text()="You have been successfully logged in"]')
}