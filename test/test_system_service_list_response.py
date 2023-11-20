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

from forester_client.models.system_service_list_response import SystemServiceListResponse

class TestSystemServiceListResponse(unittest.TestCase):
    """SystemServiceListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemServiceListResponse:
        """Test SystemServiceListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemServiceListResponse`
        """
        model = SystemServiceListResponse()
        if include_optional:
            return SystemServiceListResponse(
                systems = [
                    forester_client.models.system.System(
                        id = 1.337, 
                        name = '', 
                        hw_addrs = [
                            ''
                            ], 
                        facts = {
                            'key' : ''
                            }, 
                        acquired = True, 
                        acquired_at = '', 
                        image_id = 1.337, 
                        comment = '', 
                        appliance_id = 1.337, 
                        appliance = forester_client.models.appliance.Appliance(
                            id = 1.337, 
                            name = '', 
                            kind = 1.337, 
                            uri = '', ), 
                        uid = '', 
                        install_uuid = '', )
                    ]
            )
        else:
            return SystemServiceListResponse(
        )
        """

    def testSystemServiceListResponse(self):
        """Test SystemServiceListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
