
from api_app import app


def test_get_octocat_gists():
    # Create a Flask test client
    client = app.test_client()

    # Send GET request to the API
    response = client.get("/octocat")

    # Validate HTTP response
    assert response.status_code == 200

    # Validate JSON response
    assert response.is_json

    # Convert response to JSON
    gists = response.get_json()

    # Validate that the response is a list
    assert isinstance(gists, list)

    # Validate that each Gist contains an ID and files
    for gist in gists:
        assert "id" in gist
        assert "files" in gist
