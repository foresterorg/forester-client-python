# ErrorWebrpcRequestFailed


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
from forester-client.models.error_webrpc_request_failed import ErrorWebrpcRequestFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWebrpcRequestFailed from a JSON string
error_webrpc_request_failed_instance = ErrorWebrpcRequestFailed.from_json(json)
# print the JSON string representation of the object
print ErrorWebrpcRequestFailed.to_json()

# convert the object into a dict
error_webrpc_request_failed_dict = error_webrpc_request_failed_instance.to_dict()
# create an instance of ErrorWebrpcRequestFailed from a dict
error_webrpc_request_failed_form_dict = error_webrpc_request_failed.from_dict(error_webrpc_request_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


