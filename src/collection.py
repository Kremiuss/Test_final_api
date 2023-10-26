
header = {'api_key': 'special-key'}


class Enviroments:
    url = 'https://petstore.swagger.io/v2'

class getPet:
    uri = '/pet/'
    status_code = 200

class postPet:
    uri = '/pet'
    status_code = 200
   # pet_id = '45'
    def body (pet_id):
        body = {
             "id": f"{pet_id}",
            "category": {
             "id": f"{pet_id}",
              "name": "string"
             },
             "name": "doggie",
            "photoUrls": [
              "string"
            ],
            "tags": [
             {
               "id": f"{pet_id}",
               "name": "string"
              }
            ],
            "status": "available"
            }
        return body
class deletePet:
    uri = '/pet/'
    status_code = 200

class putPet:
    uri = '/pet'
  #  status_code = 200
    def body(pet_id):
        body = {
            "id": f"{pet_id}",
            "category": {
                "id": f"{pet_id}",
                "name": "string"
            },
            "name": "Hot_doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": f"{pet_id}",
                    "name": "string"
                }
            ],
            "status": "available"
        }
        return body

class getUser:
    uri = '/user/login'
    username = 'api_key'
    password = 'special-key'
    status_code = 200

class postStoreOrder:
    uri = '/store/order'
    def body(pet_id):
        body = {
          "id": 2,
          "petId": f"{pet_id}",
          "quantity": 0,
          "shipDate": "2023-10-24T19:28:09.864Z",
          "status": "placed",
          "complete": "true"
        }
        return body
