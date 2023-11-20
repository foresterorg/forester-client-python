# SystemServiceFindResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | [**System**](.md) |  | [optional] 

## Example

```python
from forester_client.models.system_service_find_response import SystemServiceFindResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceFindResponse from a JSON string
system_service_find_response_instance = SystemServiceFindResponse.from_json(json)
# print the JSON string representation of the object
print SystemServiceFindResponse.to_json()

# convert the object into a dict
system_service_find_response_dict = system_service_find_response_instance.to_dict()
# create an instance of SystemServiceFindResponse from a dict
system_service_find_response_form_dict = system_service_find_response.from_dict(system_service_find_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


