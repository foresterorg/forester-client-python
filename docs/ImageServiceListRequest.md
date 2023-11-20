# ImageServiceListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** |  | [optional] 
**offset** | **float** |  | [optional] 

## Example

```python
from forester_client.models.image_service_list_request import ImageServiceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageServiceListRequest from a JSON string
image_service_list_request_instance = ImageServiceListRequest.from_json(json)
# print the JSON string representation of the object
print ImageServiceListRequest.to_json()

# convert the object into a dict
image_service_list_request_dict = image_service_list_request_instance.to_dict()
# create an instance of ImageServiceListRequest from a dict
image_service_list_request_form_dict = image_service_list_request.from_dict(image_service_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


