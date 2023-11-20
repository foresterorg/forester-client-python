# ImageServiceCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**upload_path** | **str** |  | [optional] 

## Example

```python
from forester-client.models.image_service_create_response import ImageServiceCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageServiceCreateResponse from a JSON string
image_service_create_response_instance = ImageServiceCreateResponse.from_json(json)
# print the JSON string representation of the object
print ImageServiceCreateResponse.to_json()

# convert the object into a dict
image_service_create_response_dict = image_service_create_response_instance.to_dict()
# create an instance of ImageServiceCreateResponse from a dict
image_service_create_response_form_dict = image_service_create_response.from_dict(image_service_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


