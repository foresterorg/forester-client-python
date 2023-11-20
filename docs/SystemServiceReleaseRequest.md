# SystemServiceReleaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_pattern** | **str** |  | [optional] 

## Example

```python
from forester_client.models.system_service_release_request import SystemServiceReleaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceReleaseRequest from a JSON string
system_service_release_request_instance = SystemServiceReleaseRequest.from_json(json)
# print the JSON string representation of the object
print SystemServiceReleaseRequest.to_json()

# convert the object into a dict
system_service_release_request_dict = system_service_release_request_instance.to_dict()
# create an instance of SystemServiceReleaseRequest from a dict
system_service_release_request_form_dict = system_service_release_request.from_dict(system_service_release_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


