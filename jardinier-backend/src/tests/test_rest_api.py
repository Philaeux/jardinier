def test_rest_hello_world(mock_app):
    """Example of a test on the /hello endpoint"""
    response = mock_app.get('/hello')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}
