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

from forester_client.models.error_webrpc_bad_response import ErrorWebrpcBadResponse

class TestErrorWebrpcBadResponse(unittest.TestCase):
    """ErrorWebrpcBadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorWebrpcBadResponse:
        """Test ErrorWebrpcBadResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorWebrpcBadResponse`
        """
        model = ErrorWebrpcBadResponse()
        if include_optional:
            return ErrorWebrpcBadResponse(
                error = 'WebrpcBadResponse',
                code = -5,
                msg = 'bad response',
                cause = '',
                status = 500
            )
        else:
            return ErrorWebrpcBadResponse(
                error = 'WebrpcBadResponse',
                code = -5,
                msg = 'bad response',
                status = 500,
        )
        """

    def testErrorWebrpcBadResponse(self):
        """Test ErrorWebrpcBadResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
