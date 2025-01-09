"""Hometask 25."""

"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
"""

# CSS selectors:

guest_log_in_button = "div.header_right.d-flex.align-items-center button.header-link.-guest"

sign_in_button = "div.header_right.d-flex.align-items-center button.btn.btn-outline-white.header_signin"

header_logo = 'div.header_left.d-flex.align-items-center a[routerlink="/"].header_logo svg'

title_desc = "h1.hero-descriptor_title.display-2"

title_desc_text = "p.hero-descriptor_descr.lead"

hero_video = "iframe.hero-video_frame"

sign_up_button = "button.hero-descriptor_btn.btn.btn-primary"

facebook_icon = "div.contacts_socials.socials a.socials_link span.socials_icon.icon.icon-facebook"

telegram_icon = "span.socials_icon.icon.icon-telegram"

youtube_icon = "a[rel='nofollow'] span.socials_icon.icon.icon-youtube"

instagram_icon = "a[target='_blank'] span.socials_icon.icon.icon-instagram"

linkedin_icon = "div a span.socials_icon.icon.icon-linkedin"

contacts_button = "div.row div a.contacts_link.display-4"

support_button = "div.row div a.contacts_link.h4"

footer_date = "div.col-7.d-flex.flex-column.justify-content-center.footer_item.-left p:nth-of-type(1)"

footer_text = "div.col-7.d-flex.flex-column.justify-content-center.footer_item.-left p:nth-of-type(2)"

footer_logo_svg = "div.col.footer_item.-right a.footer_logo svg"

dialogue_log_in_header = "div.modal-header h4.modal-title"

close_button = "div.modal-header button[aria-label='Close'].close span"

sign_in_email_header = "div.modal-body div.form-group label[for='signinEmail']"
sign_in_email_textbox = "div.modal-body div.form-group input#signinEmail"

sign_in_password_header = "div.modal-body div.form-group label[for='signinPassword']"
sign_in_password_textbox = "div.modal-body div.form-group input#signinPassword"

forgot_password_button = ("div.modal-body div.form-group.d-flex.align-items-center."
                          "justify-content-between button.btn.btn-link")

remember_checkbox_text = "div.form-group div.form-check label[for='remember'].form-check-label"

remember_checkbox_box = "div.form-group div.form-check input#remember[formcontrolname='remember']"

registration_button = "div.modal-footer.d-flex.justify-content-between button.btn.btn-link"

login_button = "div.modal-footer.d-flex.justify-content-between button.btn.btn-primary"

my_profile_button = "div.user-nav.dropdown button#userNavDropdown"
my_profile_img = "div.user-nav.dropdown button#userNavDropdown img.icon-btn"

dropdown_garage_button_active = ("div.user-nav.show.dropdown nav.user-nav_menu.dropdown-menu."
                                 "show a[routerlink='/panel/garage'],dropdown-item."
                                 "btn.btn-link.user-nav_link disabled")
dropdown_garage_button_disabled = ("div.user-nav.show.dropdown nav.user-nav_menu."
                                   "dropdown-menu.show a[routerlink='/panel/garage'],"
                                   "dropdown-item.btn.btn-link.user-nav_link disabled")

garage_page_header = "div.panel-page div h1"

add_car_button = "div.panel-page div button.btn.btn-primary"

no_car_logo = "div.panel-page_cars div svg"

no_car_text = "div.panel-page_cars div p"

fuel_expenses_header = "div.panel-page div h1"

add_expense_button = "div.panel-page div div.item-group button.btn.btn-primary"
