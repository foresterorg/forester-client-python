# RpcImageServiceCreatePost5XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**code** | **float** |  | 
**msg** | **str** |  | 
**cause** | **str** |  | [optional] 
**status** | **float** |  | 

## Example

```python
from forester-client.models.rpc_image_service_create_post5_xx_response import RpcImageServiceCreatePost5XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RpcImageServiceCreatePost5XXResponse from a JSON string
rpc_image_service_create_post5_xx_response_instance = RpcImageServiceCreatePost5XXResponse.from_json(json)
# print the JSON string representation of the object
print RpcImageServiceCreatePost5XXResponse.to_json()

# convert the object into a dict
rpc_image_service_create_post5_xx_response_dict = rpc_image_service_create_post5_xx_response_instance.to_dict()
# create an instance of RpcImageServiceCreatePost5XXResponse from a dict
rpc_image_service_create_post5_xx_response_form_dict = rpc_image_service_create_post5_xx_response.from_dict(rpc_image_service_create_post5_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


