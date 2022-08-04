# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import luisd
from luisd.paths.api_counterparties_counterpartyagreements_scope_code import delete  # noqa: E501
from luisd import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiCounterpartiesCounterpartyagreementsScopeCode(ApiTestMixin, unittest.TestCase):
    """
    ApiCounterpartiesCounterpartyagreementsScopeCode unit test stubs
        [EXPERIMENTAL] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()