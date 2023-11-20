# ErrorWebrpcEndpoint


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
from forester-client.models.error_webrpc_endpoint import ErrorWebrpcEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWebrpcEndpoint from a JSON string
error_webrpc_endpoint_instance = ErrorWebrpcEndpoint.from_json(json)
# print the JSON string representation of the object
print ErrorWebrpcEndpoint.to_json()

# convert the object into a dict
error_webrpc_endpoint_dict = error_webrpc_endpoint_instance.to_dict()
# create an instance of ErrorWebrpcEndpoint from a dict
error_webrpc_endpoint_form_dict = error_webrpc_endpoint.from_dict(error_webrpc_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


