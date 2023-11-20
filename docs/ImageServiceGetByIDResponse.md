# ImageServiceGetByIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**Image**](Image.md) |  | [optional] 

## Example

```python
from forester_client.models.image_service_get_by_id_response import ImageServiceGetByIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageServiceGetByIDResponse from a JSON string
image_service_get_by_id_response_instance = ImageServiceGetByIDResponse.from_json(json)
# print the JSON string representation of the object
print ImageServiceGetByIDResponse.to_json()

# convert the object into a dict
image_service_get_by_id_response_dict = image_service_get_by_id_response_instance.to_dict()
# create an instance of ImageServiceGetByIDResponse from a dict
image_service_get_by_id_response_form_dict = image_service_get_by_id_response.from_dict(image_service_get_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


