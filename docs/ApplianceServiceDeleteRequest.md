# ApplianceServiceDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from forester-client.models.appliance_service_delete_request import ApplianceServiceDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceServiceDeleteRequest from a JSON string
appliance_service_delete_request_instance = ApplianceServiceDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApplianceServiceDeleteRequest.to_json()

# convert the object into a dict
appliance_service_delete_request_dict = appliance_service_delete_request_instance.to_dict()
# create an instance of ApplianceServiceDeleteRequest from a dict
appliance_service_delete_request_form_dict = appliance_service_delete_request.from_dict(appliance_service_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


