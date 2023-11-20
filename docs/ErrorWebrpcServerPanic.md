# ErrorWebrpcServerPanic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**code** | **float** |  | 
**msg** | **str** |  | 
**cause** | **str** |  | [optional] 
**status** | **float** |  | 

## Example

```python
from forester_client.models.error_webrpc_server_panic import ErrorWebrpcServerPanic

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWebrpcServerPanic from a JSON string
error_webrpc_server_panic_instance = ErrorWebrpcServerPanic.from_json(json)
# print the JSON string representation of the object
print ErrorWebrpcServerPanic.to_json()

# convert the object into a dict
error_webrpc_server_panic_dict = error_webrpc_server_panic_instance.to_dict()
# create an instance of ErrorWebrpcServerPanic from a dict
error_webrpc_server_panic_form_dict = error_webrpc_server_panic.from_dict(error_webrpc_server_panic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


