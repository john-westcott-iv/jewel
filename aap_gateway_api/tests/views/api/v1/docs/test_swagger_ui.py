from django.urls import reverse


def test_swagger_ui_marks_its_api_requests(unauthenticated_api_client):
    response = unauthenticated_api_client.get(reverse("swagger-ui"))

    assert response.status_code == 200
    assert b'request.headers["X-AAP-Swagger-UI"] = "1"' in response.content
