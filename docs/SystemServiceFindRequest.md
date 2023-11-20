# SystemServiceFindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** |  | [optional] 

## Example

```python
from forester_client.models.system_service_find_request import SystemServiceFindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceFindRequest from a JSON string
system_service_find_request_instance = SystemServiceFindRequest.from_json(json)
# print the JSON string representation of the object
print SystemServiceFindRequest.to_json()

# convert the object into a dict
system_service_find_request_dict = system_service_find_request_instance.to_dict()
# create an instance of SystemServiceFindRequest from a dict
system_service_find_request_form_dict = system_service_find_request.from_dict(system_service_find_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


