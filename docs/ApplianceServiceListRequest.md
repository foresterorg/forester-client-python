# ApplianceServiceListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** |  | [optional] 
**offset** | **float** |  | [optional] 

## Example

```python
from forester_client.models.appliance_service_list_request import ApplianceServiceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceServiceListRequest from a JSON string
appliance_service_list_request_instance = ApplianceServiceListRequest.from_json(json)
# print the JSON string representation of the object
print ApplianceServiceListRequest.to_json()

# convert the object into a dict
appliance_service_list_request_dict = appliance_service_list_request_instance.to_dict()
# create an instance of ApplianceServiceListRequest from a dict
appliance_service_list_request_form_dict = appliance_service_list_request.from_dict(appliance_service_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


