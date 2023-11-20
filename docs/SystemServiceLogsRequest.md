# SystemServiceLogsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_pattern** | **str** |  | [optional] 

## Example

```python
from forester-client.models.system_service_logs_request import SystemServiceLogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceLogsRequest from a JSON string
system_service_logs_request_instance = SystemServiceLogsRequest.from_json(json)
# print the JSON string representation of the object
print SystemServiceLogsRequest.to_json()

# convert the object into a dict
system_service_logs_request_dict = system_service_logs_request_instance.to_dict()
# create an instance of SystemServiceLogsRequest from a dict
system_service_logs_request_form_dict = system_service_logs_request.from_dict(system_service_logs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


