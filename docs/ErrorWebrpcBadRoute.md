# ErrorWebrpcBadRoute


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
from forester-client.models.error_webrpc_bad_route import ErrorWebrpcBadRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWebrpcBadRoute from a JSON string
error_webrpc_bad_route_instance = ErrorWebrpcBadRoute.from_json(json)
# print the JSON string representation of the object
print ErrorWebrpcBadRoute.to_json()

# convert the object into a dict
error_webrpc_bad_route_dict = error_webrpc_bad_route_instance.to_dict()
# create an instance of ErrorWebrpcBadRoute from a dict
error_webrpc_bad_route_form_dict = error_webrpc_bad_route.from_dict(error_webrpc_bad_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


