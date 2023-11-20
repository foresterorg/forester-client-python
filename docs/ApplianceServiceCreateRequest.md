# ApplianceServiceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**kind** | **float** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from forester-client.models.appliance_service_create_request import ApplianceServiceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceServiceCreateRequest from a JSON string
appliance_service_create_request_instance = ApplianceServiceCreateRequest.from_json(json)
# print the JSON string representation of the object
print ApplianceServiceCreateRequest.to_json()

# convert the object into a dict
appliance_service_create_request_dict = appliance_service_create_request_instance.to_dict()
# create an instance of ApplianceServiceCreateRequest from a dict
appliance_service_create_request_form_dict = appliance_service_create_request.from_dict(appliance_service_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


