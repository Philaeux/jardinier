import pytest


@pytest.mark.asyncio
async def test_qa(mock_app):
    """Test the execution of the querry qa"""

    query_success_example = """
        query querySuccessExample {
            querySuccessExample {
                __typename
            }
        }
    """

    response = mock_app.post("/graphql", headers={}, json={
        "query": query_success_example,
        "variables": {
            "fastId": "fast_simple"}})

    assert response.status_code == 200
    result_json = response.json()
    assert result_json == {'data': {'querySuccessExample': {'__typename': 'ApiSuccess'}}}
