import requests
from behave import *
from payLoad import *
from utilities.resources import *
from utilities.configurations import *
import random


# ---------------------------
# ADD BOOK API
# ---------------------------

@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}

    # Make aisle random to avoid duplicate error
    random_aisle = str(random.randint(1000, 9999))
    context.payload = addBookPayload("maddsfppt", random_aisle)


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(
        context.url,
        json=context.payload,
        headers=context.headers
    )


#@then('book is successfully added')
#def step_impl(context):
 #   print(context.response.json())
  #  response_json = context.response.json()

 #   context.bookId = response_json['ID']
 #  print(context.bookId)

  #  assert response_json["Msg"] == "successfully added"


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}

    random_aisle = str(random.randint(1000, 9999))
    context.payload = addBookPayload(isbn, random_aisle)


@then('status code of response should be 200')
def step_impl(context):
    assert context.response.status_code == 200


# ---------------------------
# PUBLIC GITHUB API (SAFE)
# ---------------------------

@given('I hit public github repo API')
def step_impl(context):
    # Public GitHub API - No auth required
    context.url = ApiResources.githubRepo


@when('I send GET request')
def step_impl(context):
    context.response = requests.get(context.url)


@then('github response status code should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
# ---------------------------
# ALLURE COMMAND
# ---------------------------
# To generate allure reports:
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports

import allure

@then('book is successfully added')
def step_impl(context):
    allure.attach(
        context.response.text,
        name="AddBook Response",
        attachment_type=allure.attachment_type.JSON
    )
    response_json = context.response.json()
    assert response_json["Msg"] == "successfully added"

#Purpose: Python code that maps each Gherkin step to actual HTTP calls