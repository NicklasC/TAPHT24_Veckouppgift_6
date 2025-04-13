from behave import when, then
import time

from playwright.sync_api import expect, Page

from tests.pages.ny_vän_page import NyvänPage
from tests.pages.vänlista_page import VänlistaPage

from tests.pages.start_page import MainPage
from tests.pages.header_page import HeaderPage


# Exist
@then(u'The {object_description} object on the {page} page should display')
def step_impl(context, object_description, page):
    page = page.lower()
    object_description = object_description.lower()

    if page == "vänlista":
        page = VänlistaPage(context.page)
        if object_description == "sök namn":
            object = page.sök_namn

    if page == "ny vän" or page == "ny_vän" or page == "nyvän":
        page = NyvänPage(context.page)
        if object_description == "namn":
            object = page.namn_edit
    try:
        expect(object).to_be_visible()
    except UnboundLocalError:
        raise Exception(
            f"Bad descriptors, The object '{object_description}' and / or the  page '{page}' was not defined in the test code.")


# Type
@when(u'I type {text} in {object_description} field on the {page} page')
def step_impl(context, text, object_description, page):
    page = page.lower()
    object_description = object_description.lower()
    if page == "ny vän" or page == "ny_vän" or page == "nyvän":
        page = NyvänPage(context.page)
        if object_description == "namn":
            object = page.namn_edit
        elif object_description == "epost" or object_description == "e-post":
            object = page.epost_edit
    try:
        object.fill(text)
    except UnboundLocalError:
        raise Exception(
            f"Bad descriptors, The object '{object_description}' and / or the  page '{page}' was not defined in the test code.")


@then(u'The spara button should be {expected_status}')
def step_impl(context, expected_status):
    page = NyvänPage(context.page)
    expected_status = expected_status.lower()
    if expected_status == "enabled":
        expect(page.save_button).to_be_enabled()
    elif expected_status == "disabled":
        expect(page.save_button).to_be_disabled()

# Click
# @when(u'I click {object_name} {object_type} on the {page} page')
# def step_impl(context, page, object_name):
#     page = page.lower()
#     object_name = object_name.lower()
#
#     if page == "start":
#         page = VänlistaPage(context.page)
#         if object_name == "vänlista":
