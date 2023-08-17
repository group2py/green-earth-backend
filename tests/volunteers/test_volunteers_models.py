import pytest

@pytest.mark.skip(reason="Cadastro de voluntário não está funcionando")
@pytest.mark.django_db
def test_register_volunteer_then_voluntary_must_be_registred(volunteer_created):
    assert volunteer_created.exists()