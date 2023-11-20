# SystemServiceLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[LogEntry]**](LogEntry.md) | []LogEntry | [optional] 

## Example

```python
from forester_client.models.system_service_logs_response import SystemServiceLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemServiceLogsResponse from a JSON string
system_service_logs_response_instance = SystemServiceLogsResponse.from_json(json)
# print the JSON string representation of the object
print SystemServiceLogsResponse.to_json()

# convert the object into a dict
system_service_logs_response_dict = system_service_logs_response_instance.to_dict()
# create an instance of SystemServiceLogsResponse from a dict
system_service_logs_response_form_dict = system_service_logs_response.from_dict(system_service_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


