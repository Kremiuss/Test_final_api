import pytest
from pytest_dependency import depends
from src.tast_data import Data
from src import requests_openapi as API


@pytest.mark.smoke
def test_add_pet():
    r = API.getPet()
    assert r.status_code == 200 or r.status_code == 404
    # assert API.getPet().response == 200 or API.getPet().response == 404
    r = API.postPet()
    assert r.status_code == 200
    #assert API.postPet().response == 200
    r = API.getPet()
    assert r.status_code == 200
    #assert API.getPet().response == 200

#@pytest.mark.dependency(depends=["test_add_pet"])
def test_put_pet():
    r = API.putPet()
    assert r.status_code == 200
    #assert API.putPet().response == 200
    r = API.getPet()
    r_dictionary = r.json()
    assert r_dictionary.get('name') == 'Hot_doggie'


#@pytest.mark.dependency(depends=["test_add_pet"])
@pytest.mark.sla
def test_sla_getPet():
    r = API.getPet()
    r_time = r.elapsed.total_seconds()
    assert r.status_code == 200
    assert r_time <= Data.sla

#@pytest.mark.dependency(depends=["test_add_pet"])
@pytest.mark.sanity
def test_delete_pet():
    r = API.getPet()
    assert r.status_code == 200
    #assert API.getPet().response == 200
    r = API.deletePet()
    assert r.status_code == 200
    #assert API.deletePet().response == 200
    r = API.getPet()
    assert r.status_code == 404
    #assert API.getPet().response == 404

def test_post_order():
    r=API.postOrderStore()
    assert r.status_code == 200
    r_dictionary = r.json()
    assert r_dictionary.get('id') == Data.order_id


@pytest.mark.sla
def test_sla_postPet():
    r = API.postPet()
    r_time = r.elapsed.total_seconds()
    assert r.status_code == 200
    assert r_time <= Data.sla

#@pytest.mark.dependency(depends=["test_sla_postPet"])
@pytest.mark.sla
def test_sla_putPet():
    r = API.putPet()
    r_time = r.elapsed.total_seconds()
    assert r.status_code == 200
    assert r_time <= Data.sla

#@pytest.mark.dependency(depends=["test_sla_postPet"])
@pytest.mark.sla
def test_sla_deletePet():
    r = API.deletePet()
    r_time = r.elapsed.total_seconds()
    assert r.status_code == 200
    assert r_time <= Data.sla




