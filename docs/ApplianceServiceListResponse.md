# ApplianceServiceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliances** | [**List[Appliance]**](Appliance.md) | []Appliance | [optional] 

## Example

```python
from forester_client.models.appliance_service_list_response import ApplianceServiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceServiceListResponse from a JSON string
appliance_service_list_response_instance = ApplianceServiceListResponse.from_json(json)
# print the JSON string representation of the object
print ApplianceServiceListResponse.to_json()

# convert the object into a dict
appliance_service_list_response_dict = appliance_service_list_response_instance.to_dict()
# create an instance of ApplianceServiceListResponse from a dict
appliance_service_list_response_form_dict = appliance_service_list_response.from_dict(appliance_service_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


