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

from forester_client.models.image_service_find_request import ImageServiceFindRequest

class TestImageServiceFindRequest(unittest.TestCase):
    """ImageServiceFindRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageServiceFindRequest:
        """Test ImageServiceFindRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageServiceFindRequest`
        """
        model = ImageServiceFindRequest()
        if include_optional:
            return ImageServiceFindRequest(
                pattern = ''
            )
        else:
            return ImageServiceFindRequest(
        )
        """

    def testImageServiceFindRequest(self):
        """Test ImageServiceFindRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
