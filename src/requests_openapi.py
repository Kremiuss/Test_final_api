import requests
from src import collection
from src.tast_data import Data

def getPet():
    response = requests.get(collection.Enviroments.url+collection.getPet.uri + Data.pet_id)
    return response

def postPet():
    response = requests.post(collection.Enviroments.url + collection.postPet.uri, json=collection.postPet.body(Data.pet_id))
    return response

def deletePet():
    response = requests.delete(collection.Enviroments.url+collection.deletePet.uri + Data.pet_id, headers=collection.header)
    return response

def putPet():
    response = requests.put(collection.Enviroments.url+collection.putPet.uri, json=collection.putPet.body(Data.pet_id))
    return response

def postOrderStore():
    response = requests.post(collection.Enviroments.url + collection.postStoreOrder.uri, json=collection.postStoreOrder.body(Data.pet_id))
    return response