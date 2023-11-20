# SnippetServiceFindResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snippet** | [**Snippet**](.md) |  | [optional] 

## Example

```python
from forester-client.models.snippet_service_find_response import SnippetServiceFindResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetServiceFindResponse from a JSON string
snippet_service_find_response_instance = SnippetServiceFindResponse.from_json(json)
# print the JSON string representation of the object
print SnippetServiceFindResponse.to_json()

# convert the object into a dict
snippet_service_find_response_dict = snippet_service_find_response_instance.to_dict()
# create an instance of SnippetServiceFindResponse from a dict
snippet_service_find_response_form_dict = snippet_service_find_response.from_dict(snippet_service_find_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


