# SystemServiceAcquireRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_pattern** | **str** |  | [optional] 
**image_pattern** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**snippets** | **List[str]** | []string | [optional] 
**custom_snippet** | **str** |  | [optional] 

## Example

```python
from forester_client.models.system_service_acquire_request import SystemServiceAcquireRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceAcquireRequest from a JSON string
system_service_acquire_request_instance = SystemServiceAcquireRequest.from_json(json)
# print the JSON string representation of the object
print SystemServiceAcquireRequest.to_json()

# convert the object into a dict
system_service_acquire_request_dict = system_service_acquire_request_instance.to_dict()
# create an instance of SystemServiceAcquireRequest from a dict
system_service_acquire_request_form_dict = system_service_acquire_request.from_dict(system_service_acquire_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


