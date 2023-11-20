import time
import os
import forester_client
from forester_client.models.appliance_service_list_request import ApplianceServiceListRequest
from forester_client.models.appliance_service_list_response import ApplianceServiceListResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
        host = "http://zzzap.tpb.lab.eng.brq.redhat.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    appliance_service_list_request = forester_client.ApplianceServiceListRequest() # ApplianceServiceListRequest |  (optional)

    try:
        api_response = api_instance.rpc_appliance_service_list_post(appliance_service_list_request=appliance_service_list_request)
        print("The response of DefaultApi->rpc_appliance_service_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_appliance_service_list_post: %s\n" % e)
