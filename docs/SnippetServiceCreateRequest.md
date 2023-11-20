# SnippetServiceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**kind** | **float** |  | [optional] 
**body** | **str** |  | [optional] 

## Example

```python
from forester_client.models.snippet_service_create_request import SnippetServiceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetServiceCreateRequest from a JSON string
snippet_service_create_request_instance = SnippetServiceCreateRequest.from_json(json)
# print the JSON string representation of the object
print SnippetServiceCreateRequest.to_json()

# convert the object into a dict
snippet_service_create_request_dict = snippet_service_create_request_instance.to_dict()
# create an instance of SnippetServiceCreateRequest from a dict
snippet_service_create_request_form_dict = snippet_service_create_request.from_dict(snippet_service_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


