# System


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**hw_addrs** | **List[str]** | []string | 
**facts** | **Dict[str, str]** | map&lt;string,string&gt; | 
**acquired** | **bool** |  | 
**acquired_at** | **str** |  | 
**image_id** | **float** |  | [optional] 
**comment** | **str** |  | 
**appliance_id** | **float** |  | [optional] 
**appliance** | [**Appliance**](Appliance.md) |  | [optional] 
**uid** | **str** |  | [optional] 
**install_uuid** | **str** |  | 

## Example

```python
from forester_client.models.system import System

# TODO update the JSON string below
json = "{}"
# create an instance of System from a JSON string
system_instance = System.from_json(json)
# print the JSON string representation of the object
print System.to_json()

# convert the object into a dict
system_dict = system_instance.to_dict()
# create an instance of System from a dict
system_form_dict = system.from_dict(system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


