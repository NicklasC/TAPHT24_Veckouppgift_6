from behave import when, then
import time

from playwright.sync_api import expect, Page

from tests.pages.vänlista_page import VänlistaPage
from tests.pages.start_page import MainPage
from tests.pages.header_page import HeaderPage

@when(u'I navigate to the URL "{url}"')
def step_impl(context, url):
    context.page.goto(url)  #
    time.sleep(5)

@when(u'I click {location} in the header')
def step_impl(context, location):
    location = location.lower()
    page = HeaderPage(context.page)

    if location=="start":
        page.start_link.click()
    elif location=="vänlista":
        page.vänlista_link.click()
    elif location=="ny vän" or location=="ny_vän":
        page.ny_vän_link.click()


@then(u'the start page should display')
def step_impl(context):
    main_page = MainPage(context.page)
    expect(main_page.title).to_have_text("Mina vänner")

    # raise NotImplementedError(u'STEP: Then the start page should display')
