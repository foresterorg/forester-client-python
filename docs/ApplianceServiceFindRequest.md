# ApplianceServiceFindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from forester_client.models.appliance_service_find_request import ApplianceServiceFindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceServiceFindRequest from a JSON string
appliance_service_find_request_instance = ApplianceServiceFindRequest.from_json(json)
# print the JSON string representation of the object
print ApplianceServiceFindRequest.to_json()

# convert the object into a dict
appliance_service_find_request_dict = appliance_service_find_request_instance.to_dict()
# create an instance of ApplianceServiceFindRequest from a dict
appliance_service_find_request_form_dict = appliance_service_find_request.from_dict(appliance_service_find_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


