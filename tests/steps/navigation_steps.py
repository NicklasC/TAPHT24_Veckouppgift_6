from behave import when, then
import time

from pages.main_page import MainPage
from playwright.sync_api import expect, Page


@when(u'I navigate to the URL "{url}"')
def step_impl(context,url):
    context.page.goto(url)  #
    time.sleep(5)


@then(u'the start page should display')
def step_impl(context):
    main_page = MainPage(context.page)
    expect(main_page.title).to_have_text("Mina vänner")

    #raise NotImplementedError(u'STEP: Then the start page should display')
