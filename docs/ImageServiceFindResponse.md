# ImageServiceFindResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**Image**](.md) |  | [optional] 

## Example

```python
from forester_client.models.image_service_find_response import ImageServiceFindResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageServiceFindResponse from a JSON string
image_service_find_response_instance = ImageServiceFindResponse.from_json(json)
# print the JSON string representation of the object
print ImageServiceFindResponse.to_json()

# convert the object into a dict
image_service_find_response_dict = image_service_find_response_instance.to_dict()
# create an instance of ImageServiceFindResponse from a dict
image_service_find_response_form_dict = image_service_find_response.from_dict(image_service_find_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


