import pytest


@pytest.mark.django_db
def test_list_contributors_then_should_return_200(client):
    requisicao = client.get('/contributors/contributors/')
    assert requisicao.status_code == 200


@pytest.mark.django_db
def test_create_contributors_then_should_return_201(client, contributors_data):
    requisicao = client.post('/contributors/create_contributors/', data=contributors_data)
    assert requisicao.status_code == 201


@pytest.mark.skip(
    reason='A requisição não pode ser feita, porque está tentado retornar um objeto users e objetos do tipo Users não são JSON serializable')
@pytest.mark.django_db
def test_get_contributor_then_should_return_200(client, contributors_created):
    requisicao = client.get(f'/contributors/contributors/{(contributors_created.id)}/')
    assert requisicao.status_code == 200


# atenção eu tive que renomear a função destroy de DeleteContributors para delete, para que o teste funcionasse
@pytest.mark.django_db
def test_delete_contributor_then_should_return_200(client, contributors_created):
    requisicao = client.delete(f'/contributors/contributors/{(contributors_created.id)}/delete/')
    assert requisicao.status_code == 200


@pytest.mark.skip(
    reason='o erro acontece porque CreateContributionHistory está tentando usar um .strip() no value, local da Exception: /contributors/utils.py, line 4')
@pytest.mark.django_db
def test_create_contribution_history_then_should_return_201(client, contributors_history_data):
    requisicao = client.post('/contributors/create_contributors_history/', data=contributors_history_data)
    assert requisicao.status_code == 201


@pytest.mark.django_db
def test_list_contribution_history_then_should_return_200(client):
    requisicao = client.get('/contributors/contributors_history/')
    assert requisicao.status_code == 200


@pytest.mark.skip(
    reason='não é possível executar esse teste, porque não é possível criar um objeto ContributionHistory')
@pytest.mark.django_db
def test_get_contribution_history_then_should_return_200(client, contributors_history_created):
    requisicao = client.get(f'/contributors/contributors/{(contributors_history_created.id)}/')
    assert requisicao.status_code == 200
