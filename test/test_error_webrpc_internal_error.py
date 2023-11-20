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

from forester_client.models.error_webrpc_internal_error import ErrorWebrpcInternalError

class TestErrorWebrpcInternalError(unittest.TestCase):
    """ErrorWebrpcInternalError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorWebrpcInternalError:
        """Test ErrorWebrpcInternalError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorWebrpcInternalError`
        """
        model = ErrorWebrpcInternalError()
        if include_optional:
            return ErrorWebrpcInternalError(
                error = 'WebrpcInternalError',
                code = -7,
                msg = 'internal error',
                cause = '',
                status = 500
            )
        else:
            return ErrorWebrpcInternalError(
                error = 'WebrpcInternalError',
                code = -7,
                msg = 'internal error',
                status = 500,
        )
        """

    def testErrorWebrpcInternalError(self):
        """Test ErrorWebrpcInternalError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()