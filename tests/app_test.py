def test_get_server(client):
    response = client.get(
        '/',
    )

    assert response.status_code == 200