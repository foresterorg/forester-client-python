# SystemServiceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**systems** | [**List[System]**](System.md) | []System | [optional] 

## Example

```python
from forester-client.models.system_service_list_response import SystemServiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceListResponse from a JSON string
system_service_list_response_instance = SystemServiceListResponse.from_json(json)
# print the JSON string representation of the object
print SystemServiceListResponse.to_json()

# convert the object into a dict
system_service_list_response_dict = system_service_list_response_instance.to_dict()
# create an instance of SystemServiceListResponse from a dict
system_service_list_response_form_dict = system_service_list_response.from_dict(system_service_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


