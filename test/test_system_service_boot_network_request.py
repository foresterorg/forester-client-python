# coding: utf-8

"""
    ImageService API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from forester_client.models.system_service_boot_network_request import SystemServiceBootNetworkRequest

class TestSystemServiceBootNetworkRequest(unittest.TestCase):
    """SystemServiceBootNetworkRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemServiceBootNetworkRequest:
        """Test SystemServiceBootNetworkRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemServiceBootNetworkRequest`
        """
        model = SystemServiceBootNetworkRequest()
        if include_optional:
            return SystemServiceBootNetworkRequest(
                system_pattern = ''
            )
        else:
            return SystemServiceBootNetworkRequest(
        )
        """

    def testSystemServiceBootNetworkRequest(self):
        """Test SystemServiceBootNetworkRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()