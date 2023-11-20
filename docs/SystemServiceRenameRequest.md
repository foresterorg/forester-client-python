# SystemServiceRenameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** |  | [optional] 
**new_name** | **str** |  | [optional] 

## Example

```python
from forester_client.models.system_service_rename_request import SystemServiceRenameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceRenameRequest from a JSON string
system_service_rename_request_instance = SystemServiceRenameRequest.from_json(json)
# print the JSON string representation of the object
print SystemServiceRenameRequest.to_json()

# convert the object into a dict
system_service_rename_request_dict = system_service_rename_request_instance.to_dict()
# create an instance of SystemServiceRenameRequest from a dict
system_service_rename_request_form_dict = system_service_rename_request.from_dict(system_service_rename_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


