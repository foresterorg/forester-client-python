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

from forester_client.models.snippet_service_list_request import SnippetServiceListRequest

class TestSnippetServiceListRequest(unittest.TestCase):
    """SnippetServiceListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnippetServiceListRequest:
        """Test SnippetServiceListRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnippetServiceListRequest`
        """
        model = SnippetServiceListRequest()
        if include_optional:
            return SnippetServiceListRequest(
                limit = 1.337,
                offset = 1.337
            )
        else:
            return SnippetServiceListRequest(
        )
        """

    def testSnippetServiceListRequest(self):
        """Test SnippetServiceListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()