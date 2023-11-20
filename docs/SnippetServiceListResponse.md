# SnippetServiceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snippets** | [**List[Snippet]**](Snippet.md) | []Snippet | [optional] 

## Example

```python
from forester-client.models.snippet_service_list_response import SnippetServiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetServiceListResponse from a JSON string
snippet_service_list_response_instance = SnippetServiceListResponse.from_json(json)
# print the JSON string representation of the object
print SnippetServiceListResponse.to_json()

# convert the object into a dict
snippet_service_list_response_dict = snippet_service_list_response_instance.to_dict()
# create an instance of SnippetServiceListResponse from a dict
snippet_service_list_response_form_dict = snippet_service_list_response.from_dict(snippet_service_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


