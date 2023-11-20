# Appliance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**kind** | **float** |  | 
**uri** | **str** |  | 

## Example

```python
from forester-client.models.appliance import Appliance

# TODO update the JSON string below
json = "{}"
# create an instance of Appliance from a JSON string
appliance_instance = Appliance.from_json(json)
# print the JSON string representation of the object
print Appliance.to_json()

# convert the object into a dict
appliance_dict = appliance_instance.to_dict()
# create an instance of Appliance from a dict
appliance_form_dict = appliance.from_dict(appliance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


