import requests
from utilities.resources import ApiResources
from utilities.configurations import getConfig


#def after_scenario(context, scenario):
#   if hasattr(context, "bookId"):

#       delete_url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
#
#       response = requests.post(
#          delete_url,
#         json={"ID": context.bookId},
#        headers={"Content-Type": "application/json"}   )
#  assert response.status_code == 200

import requests


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

            "ID": context.bookId
        }, headers={"Content-Type": "application/json"},
                                        )

        assert response_deleteBook.status_code == 200
        res_json = response_deleteBook.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"

#Purpose: Setup/teardown hooks — code that runs before/after each scenario or feature