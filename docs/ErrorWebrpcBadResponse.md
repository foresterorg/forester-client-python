# ErrorWebrpcBadResponse


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
from forester_client.models.error_webrpc_bad_response import ErrorWebrpcBadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWebrpcBadResponse from a JSON string
error_webrpc_bad_response_instance = ErrorWebrpcBadResponse.from_json(json)
# print the JSON string representation of the object
print ErrorWebrpcBadResponse.to_json()

# convert the object into a dict
error_webrpc_bad_response_dict = error_webrpc_bad_response_instance.to_dict()
# create an instance of ErrorWebrpcBadResponse from a dict
error_webrpc_bad_response_form_dict = error_webrpc_bad_response.from_dict(error_webrpc_bad_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


