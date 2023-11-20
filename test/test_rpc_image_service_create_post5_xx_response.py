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

from forester_client.models.rpc_image_service_create_post5_xx_response import RpcImageServiceCreatePost5XXResponse

class TestRpcImageServiceCreatePost5XXResponse(unittest.TestCase):
    """RpcImageServiceCreatePost5XXResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RpcImageServiceCreatePost5XXResponse:
        """Test RpcImageServiceCreatePost5XXResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RpcImageServiceCreatePost5XXResponse`
        """
        model = RpcImageServiceCreatePost5XXResponse()
        if include_optional:
            return RpcImageServiceCreatePost5XXResponse(
                error = 'WebrpcInternalError',
                code = -7,
                msg = 'internal error',
                cause = '',
                status = 500
            )
        else:
            return RpcImageServiceCreatePost5XXResponse(
                error = 'WebrpcInternalError',
                code = -7,
                msg = 'internal error',
                status = 500,
        )
        """

    def testRpcImageServiceCreatePost5XXResponse(self):
        """Test RpcImageServiceCreatePost5XXResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
