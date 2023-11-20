# SnippetServiceListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** |  | [optional] 
**offset** | **float** |  | [optional] 

## Example

```python
from forester-client.models.snippet_service_list_request import SnippetServiceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetServiceListRequest from a JSON string
snippet_service_list_request_instance = SnippetServiceListRequest.from_json(json)
# print the JSON string representation of the object
print SnippetServiceListRequest.to_json()

# convert the object into a dict
snippet_service_list_request_dict = snippet_service_list_request_instance.to_dict()
# create an instance of SnippetServiceListRequest from a dict
snippet_service_list_request_form_dict = snippet_service_list_request.from_dict(snippet_service_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


