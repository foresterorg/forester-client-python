# SnippetServiceEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**body** | **str** |  | [optional] 

## Example

```python
from forester_client.models.snippet_service_edit_request import SnippetServiceEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetServiceEditRequest from a JSON string
snippet_service_edit_request_instance = SnippetServiceEditRequest.from_json(json)
# print the JSON string representation of the object
print SnippetServiceEditRequest.to_json()

# convert the object into a dict
snippet_service_edit_request_dict = snippet_service_edit_request_instance.to_dict()
# create an instance of SnippetServiceEditRequest from a dict
snippet_service_edit_request_form_dict = snippet_service_edit_request.from_dict(snippet_service_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


