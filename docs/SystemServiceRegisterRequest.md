# SystemServiceRegisterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system** | [**NewSystem**](.md) |  | [optional] 

## Example

```python
from forester-client.models.system_service_register_request import SystemServiceRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceRegisterRequest from a JSON string
system_service_register_request_instance = SystemServiceRegisterRequest.from_json(json)
# print the JSON string representation of the object
print SystemServiceRegisterRequest.to_json()

# convert the object into a dict
system_service_register_request_dict = system_service_register_request_instance.to_dict()
# create an instance of SystemServiceRegisterRequest from a dict
system_service_register_request_form_dict = system_service_register_request.from_dict(system_service_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


