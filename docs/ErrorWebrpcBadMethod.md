# ErrorWebrpcBadMethod


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
from forester-client.models.error_webrpc_bad_method import ErrorWebrpcBadMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWebrpcBadMethod from a JSON string
error_webrpc_bad_method_instance = ErrorWebrpcBadMethod.from_json(json)
# print the JSON string representation of the object
print ErrorWebrpcBadMethod.to_json()

# convert the object into a dict
error_webrpc_bad_method_dict = error_webrpc_bad_method_instance.to_dict()
# create an instance of ErrorWebrpcBadMethod from a dict
error_webrpc_bad_method_form_dict = error_webrpc_bad_method.from_dict(error_webrpc_bad_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


