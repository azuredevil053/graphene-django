import pytest

from .. import GraphQLTestCase
from ...tests.test_types import with_local_registry
from django.test import Client


@with_local_registry
def test_graphql_test_case_deprecated_client_getter():
    """
    `GraphQLTestCase._client`' getter should raise pending deprecation warning.
    """

    class TestClass(GraphQLTestCase):
        GRAPHQL_SCHEMA = True

        def runTest(self):
            pass

    tc = TestClass()
    tc._pre_setup()
    tc.setUpClass()

    with pytest.warns(PendingDeprecationWarning):
        tc._client


@with_local_registry
def test_graphql_test_case_deprecated_client_setter():
    """
    `GraphQLTestCase._client`' setter should raise pending deprecation warning.
    """

    class TestClass(GraphQLTestCase):
        GRAPHQL_SCHEMA = True

        def runTest(self):
            pass

    tc = TestClass()
    tc._pre_setup()
    tc.setUpClass()

    with pytest.warns(PendingDeprecationWarning):
        tc._client = Client()
