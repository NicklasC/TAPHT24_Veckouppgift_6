from behave import when, then
import time

@when(u'I navigate to the URL "{url}"')
def step_impl(context,url):
    context.page.goto(url)  #
    time.sleep(5)


@then(u'the start page should display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the start page should display')
