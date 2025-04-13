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

    if page =="ny vän" or page == "ny_vän" or page=="nyvän":
        page=NyvänPage(context.page)
        if object_description == "namn":
            object=page.namn_edit
    try:
        expect(object).to_be_visible()
    except UnboundLocalError:
        raise Exception(f"Bad descriptors, The object '{object_description}' and / or the  page '{page}' was not defined in the test code.")

# Click
# @when(u'I click {object_name} {object_type} on the {page} page')
# def step_impl(context, page, object_name):
#     page = page.lower()
#     object_name = object_name.lower()
#
#     if page == "start":
#         page = VänlistaPage(context.page)
#         if object_name == "vänlista":
