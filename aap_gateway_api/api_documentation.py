"""Gateway-specific API documentation views."""

from drf_spectacular.views import SpectacularSwaggerView

SWAGGER_UI_REQUEST_HEADER = "X-AAP-Swagger-UI"
SWAGGER_UI_REQUEST_HEADER_VALUE = "1"


class GatewaySwaggerView(SpectacularSwaggerView):
    """Swagger UI configured to identify its API requests to Gateway."""

    template_name_js = "aap_gateway_api/swagger_ui.js"
