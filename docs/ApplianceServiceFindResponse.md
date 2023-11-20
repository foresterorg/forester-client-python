# ApplianceServiceFindResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance** | [**Appliance**](.md) |  | [optional] 

## Example

```python
from forester-client.models.appliance_service_find_response import ApplianceServiceFindResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceServiceFindResponse from a JSON string
appliance_service_find_response_instance = ApplianceServiceFindResponse.from_json(json)
# print the JSON string representation of the object
print ApplianceServiceFindResponse.to_json()

# convert the object into a dict
appliance_service_find_response_dict = appliance_service_find_response_instance.to_dict()
# create an instance of ApplianceServiceFindResponse from a dict
appliance_service_find_response_form_dict = appliance_service_find_response.from_dict(appliance_service_find_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


