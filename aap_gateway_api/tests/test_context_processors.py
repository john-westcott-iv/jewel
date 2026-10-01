from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
from django.test import RequestFactory

from aap_gateway_api.context_processors import version


@pytest.mark.parametrize(
    ("html_safe", "expected"),
    [
        (False, False),
        (True, True),
    ],
)
def test_deprecation_message_html_safe_context(html_safe, expected):
    request = RequestFactory().get("/")
    request.parser_context = {
        "view": SimpleNamespace(
            deprecated=True,
            deprecated_message_html_safe=html_safe,
        ),
    }

    with patch("aap_gateway_api.context_processors.get_api_version", return_value="1.0"):
        context = version(request)

    assert context["deprecated_message_html_safe"] is expected


def test_schema_deprecation_check_swallows_attribute_errors():
    """Cover the AttributeError/TypeError guard in _check_schema_deprecation."""
    request = RequestFactory().get("/")
    schema = MagicMock()
    schema.is_deprecated.side_effect = AttributeError("boom")
    request.parser_context = {
        "view": SimpleNamespace(
            schema=schema,
            deprecated=False,
            get_serializer_class=lambda: SimpleNamespace(_spectacular_annotation="not-a-dict"),
        ),
    }

    with patch("aap_gateway_api.context_processors.get_api_version", return_value="1.0"):
        context = version(request)

    assert context["deprecated"] is False
    assert context["deprecated_message"] == ""
