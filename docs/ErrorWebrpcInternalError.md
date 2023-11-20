# ErrorWebrpcInternalError


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
from forester_client.models.error_webrpc_internal_error import ErrorWebrpcInternalError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWebrpcInternalError from a JSON string
error_webrpc_internal_error_instance = ErrorWebrpcInternalError.from_json(json)
# print the JSON string representation of the object
print ErrorWebrpcInternalError.to_json()

# convert the object into a dict
error_webrpc_internal_error_dict = error_webrpc_internal_error_instance.to_dict()
# create an instance of ErrorWebrpcInternalError from a dict
error_webrpc_internal_error_form_dict = error_webrpc_internal_error.from_dict(error_webrpc_internal_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


