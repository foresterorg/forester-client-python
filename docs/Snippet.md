# Snippet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**kind** | **float** |  | 
**body** | **str** |  | 

## Example

```python
from forester-client.models.snippet import Snippet

# TODO update the JSON string below
json = "{}"
# create an instance of Snippet from a JSON string
snippet_instance = Snippet.from_json(json)
# print the JSON string representation of the object
print Snippet.to_json()

# convert the object into a dict
snippet_dict = snippet_instance.to_dict()
# create an instance of Snippet from a dict
snippet_form_dict = snippet.from_dict(snippet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


