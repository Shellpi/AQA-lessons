"""Hometask 25."""

"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
"""

# X-Path locators:

sign_in_button = ("//div[@class='header_right d-flex align-items-center']"
                  "/button[@class = 'btn btn-outline-white header_signin']"
                  "[text() = 'Sign In']")

guest_log_in_button = ("//div[@class='header_right d-flex align-items-center']"
                       "/button[@class = 'header-link -guest']"
                       "[text() = 'Guest log in']")

header_logo_class = ("//div[@class='header_left d-flex align-items-center']"
                     "/a[@class = 'header_logo']")

header_logo = ("//div[@class='header_left d-flex align-items-center']"
               "/a[@class = 'header_logo']/*[name() = 'svg']")

header_description = "//h1[@class = 'hero-descriptor_title display-2'][text() = 'Do more!']"

text_description_contains = ("//div[@class='hero-descriptor']"
                             "/p[@class = 'hero-descriptor_descr lead']"
                             "[contains(text(), 'Hillel')]")

hero_video = "//div[@class='hero-video']/iframe[@class = 'hero-video_frame']"

sign_up_button_text = "//button[text() = 'Sign up']"
sign_up_button_class = "//button[@class = 'hero-descriptor_btn btn btn-primary']"
sign_up_button = "//button[@class = 'hero-descriptor_btn btn btn-primary'][text() = 'Sign up']"

about_block_header_text = "//p[text() = 'Log fuel expenses']"
about_block_header = "//p[@class='about-block_title h2'][text() = 'Log fuel expenses']"

about_text = "//p[contains (text(), 'Keep')]"
about_text_comb = "//p[@class='about-block_descr lead'][contains(text(), 'Keep track')]"

about_picture_1 = "//img[@class='about-picture_img'][1]"

about_picture_2 = "//img[@class='about-picture_img'][2]"

about_block_header_2_text = "//p[text() = 'Instructions and manuals']"
about_block_header_2 = "//p [@class = 'about-block_title h2'][text()='Instructions and manuals']"

about_2_text = "//p[contains (text(), 'Watch over')]"
about_2_text_comb = "//p[@class='about-block_descr lead'][contains(text(), 'Watch over')]"

contacts_header = "//h2[text()='Contacts']"

facebook_parent = "//span[@class='socials_icon icon icon-facebook']//.."
facebook_icon = "//span[@class='socials_icon icon icon-facebook']"

telegram_icon = "//span[@class='socials_icon icon icon-telegram']"
telegram_parent = "//span[@class='socials_icon icon icon-telegram']//.."

youtube_icon = "//span[@class='socials_icon icon icon-youtube']"
youtube_parent = "//span[@class='socials_icon icon icon-youtube']//.."

instagram_icon = "//span[@class='socials_icon icon icon-instagram']"
instagram_parent = "//span[@class='socials_icon icon icon-instagram']//.."

linkedin_icon = "//span[@class='socials_icon icon icon-linkedin']"
linkedin_parent = "//span[@class='socials_icon icon icon-linkedin']//.."

contacts_button_class = "//a[@class='contacts_link display-4']"
contacts_button = "//a[@class='contacts_link display-4'][text()='ithillel.ua']"

support_button_class = "//a[@class='contacts_link h4']"
support_button = "//a[@class='contacts_link h4'][text()='support@ithillel.ua']"

footer_date = "//p[text()='© 2021 Hillel IT school']"
footer_date_contains = "//p[contains(text(),'©') and contains(text(), 'Hillel IT school')]"

footer_text = ("//div[@class='col-7 d-flex flex-column justify-content-center footer_item -left']"
               "/p[contains(text(), 'Hillel') and contains(text(), 'QA courses') and contains(text(), 'educational')]")

footer_logo = "//div[@class='col footer_item -right']/a[@class='footer_logo']/*[name()='svg']"

dialogue_log_in_header_class = "//h4[@class='modal-title']"
dialogue_log_in_header = "//h4[@class='modal-title'][text()='Log in']"

close_button = "//div[@class='modal-header']/button[@class='close']"

sign_in_email_header = "//div[@class='form-group']/label[text()='Email']"
sign_in_email_textbox = "//div[@class='form-group']/input[@name='email'][@id='signinEmail']"

sign_in_password_header = "//label[text()='Password']"
sign_in_password_textbox = "//input[@name='password'][@id='signinPassword']"

forgot_password_text = "//button[text()='Forgot password']"
forgot_password_button = "//button[@class='btn btn-link'][text()='Forgot password']"

remember_checkbox_class = "//label[@class='form-check-label']"
remember_checkbox_text = "//label[@class='form-check-label'][text()=' Remember me ']"

remember_checkbox_box = ("//input[@type='checkbox'][@id='remember']"
                         "[@class='form-check-input ng-untouched ng-pristine ng-valid']")

registration_button = "//button[@class='btn btn-link'][text()='Registration']"

login_button = "//button[@class='btn btn-primary'][text()='Login']"

my_profile_button_text = "//button[text()=' My profile ']"
my_profile_img = "//img[@class='icon-btn'][@alt='User photo']"

dropdown_garage_button_active = ("//a[@routerlink='/panel/garage'][@routerlinkactive='-active']"
                                 "[text()='Garage']")
dropdown_garage_button_disabled = ("//a[@routerlink='/panel/garage'][@routerlinkactive='disabled']"
                                   "[text()='Garage']")

dropdown_fuel_exp_button_active = ("//a[@routerlink='/panel/expenses'][@routerlinkactive='-active']"
                                   "[text()='Fuel expenses']")
dropdown_fuel_exp_button_disabled = ("//a[@routerlink='/panel/expenses'][@routerlinkactive='disabled']"
                                     "[text()='Fuel expenses']")

dropdown_instructions_button_active = ("//a[@routerlink='/panel/instructions'][@routerlinkactive='-active']"
                                       "[text()='Instructions']")
dropdown_instructions_button_disabled = ("//a[@routerlink='/panel/instructions'][@routerlinkactive='disabled']"
                                         "[text()='Instructions']")

dropdown_divider_element = "//div[@class='dropdown-divider']"

dropdown_logout_button = "//button[@class='dropdown-item btn btn-link user-nav_link'][text()='Logout']"

garage_page_header = "//h1[text()='Garage']"

add_car_button = "//button[@class='btn btn-primary'][text()='Add car']"

no_car_logo = "//div[@class = 'panel-page_empty panel-empty']/*[name() = 'svg']"

no_car_text = "//p[@class='h3 panel-empty_message'][text()='You don’t have any cars in your garage']"

fuel_expenses_header = "//div/h1[text()='Fuel expenses']"

add_expense_button = "//div/button[@class='btn btn-primary'][text()='Add an expense']"

no_car_text_fuel = "//div/p[@class='h3 panel-empty_message'][text()='You don’t have any cars in ']"
your_garage_link = "//p/a[@routerlink='/panel/garage'][text()='your garage']"

instructions_header = ("//div[@class='panel-page_heading d-flex justify-content-between']"
                       "/h1[text()='Instructions']")

instructions_search_button = ("//div/button[@class='instructions-search-controls_search btn btn-primary']"
                              "[text()='Search']")

brand_selector_dropdown = "//button[@id = 'brandSelectDropdown']"

audi_select_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                     "/li[text()='Audi']")
selected_audi_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                       "/li[@class='dropdown-item btn btn-link brand-select-dropdown_item -active disabled']"
                       "[text()='Audi']")

bmw_select_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                    "/li[text()='BMW']")
selected_bmw_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']/"
                      "li[@class='dropdown-item btn btn-link brand-select-dropdown_item -active disabled']"
                      "[text()='BMW']")

ford_select_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                     "/li[text()='Ford']")
selected_ford_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                       "/li[@class='dropdown-item btn btn-link brand-select-dropdown_item -active disabled']"
                       "[text()='Ford']")

porsche_select_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                        "/li[text()='Porsche']")
selected_porsche_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                          "/li[@class='dropdown-item btn btn-link brand-select-dropdown_item -active disabled']"
                          "[text()='Porsche']")

fiat_select_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                     "/li[text()='Fiat']")
selected_fiat_brand = ("//ul[@class='brand-select-dropdown_menu dropdown-menu show']"
                       "/li[@class='dropdown-item btn btn-link brand-select-dropdown_item -active disabled']"
                       "[text()='Fiat']")

model_select_button = "//*[@id='modelSelectDropdown']"
