# ImageServiceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**Image**](Image.md) |  | [optional] 

## Example

```python
from forester_client.models.image_service_create_request import ImageServiceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageServiceCreateRequest from a JSON string
image_service_create_request_instance = ImageServiceCreateRequest.from_json(json)
# print the JSON string representation of the object
print ImageServiceCreateRequest.to_json()

# convert the object into a dict
image_service_create_request_dict = image_service_create_request_instance.to_dict()
# create an instance of ImageServiceCreateRequest from a dict
image_service_create_request_form_dict = image_service_create_request.from_dict(image_service_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


