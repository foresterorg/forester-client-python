# NewSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**hw_addrs** | **List[str]** | []string | 
**facts** | **Dict[str, str]** | map&lt;string,string&gt; | 
**appliance_name** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from forester_client.models.new_system import NewSystem

# TODO update the JSON string below
json = "{}"
# create an instance of NewSystem from a JSON string
new_system_instance = NewSystem.from_json(json)
# print the JSON string representation of the object
print NewSystem.to_json()

# convert the object into a dict
new_system_dict = new_system_instance.to_dict()
# create an instance of NewSystem from a dict
new_system_form_dict = new_system.from_dict(new_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


