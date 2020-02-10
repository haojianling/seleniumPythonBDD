from behave import *
from features.lib.pages.register_page import RegisterPage
use_step_matcher('re')
@when('I open the register website "([^"]*)"')
def step_register(context,url):
    RegisterPage(context.driver).get_url(url)
    # context.driver.get(url)

@then('I except that the title is "([^"]*)"')
def step_register1(context,title_name):
    title=RegisterPage(context.driver).get_title()
    assert title_name in title

@when('I set with useremail "([^"]*)"')
def step_register1(context,useremail):
    RegisterPage(context.driver).send_useremail(useremail)


@when('I set with username "([^"]*)"')
def step_register1(context,username):
    RegisterPage(context.driver).send_username(username)

@when('I set with password "([^"]*)"')
def step_register1(context,password):
    RegisterPage(context.driver).send_password(password)

@when('I set with code "([^"]*)"')
def step_register1(context,code):
    RegisterPage(context.driver).send_code(code)

@when('I click with registerbutton')
def step_register1(context):
    RegisterPage(context.driver).click_register_button()

@Then('I except that text "([^"]*)"')
def step_register1(context,code_error):
    text=RegisterPage(context.driver).get_code_text()
    assert code_error in text