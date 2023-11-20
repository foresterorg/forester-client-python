# forester_client.DefaultApi

All URIs are relative to *https://forester.example.com:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpc_appliance_service_create_post**](DefaultApi.md#rpc_appliance_service_create_post) | **POST** /rpc/ApplianceService/Create | 
[**rpc_appliance_service_delete_post**](DefaultApi.md#rpc_appliance_service_delete_post) | **POST** /rpc/ApplianceService/Delete | 
[**rpc_appliance_service_enlist_post**](DefaultApi.md#rpc_appliance_service_enlist_post) | **POST** /rpc/ApplianceService/Enlist | 
[**rpc_appliance_service_find_post**](DefaultApi.md#rpc_appliance_service_find_post) | **POST** /rpc/ApplianceService/Find | 
[**rpc_appliance_service_list_post**](DefaultApi.md#rpc_appliance_service_list_post) | **POST** /rpc/ApplianceService/List | 
[**rpc_image_service_create_post**](DefaultApi.md#rpc_image_service_create_post) | **POST** /rpc/ImageService/Create | 
[**rpc_image_service_delete_post**](DefaultApi.md#rpc_image_service_delete_post) | **POST** /rpc/ImageService/Delete | 
[**rpc_image_service_find_post**](DefaultApi.md#rpc_image_service_find_post) | **POST** /rpc/ImageService/Find | 
[**rpc_image_service_get_by_id_post**](DefaultApi.md#rpc_image_service_get_by_id_post) | **POST** /rpc/ImageService/GetByID | 
[**rpc_image_service_list_post**](DefaultApi.md#rpc_image_service_list_post) | **POST** /rpc/ImageService/List | 
[**rpc_snippet_service_create_post**](DefaultApi.md#rpc_snippet_service_create_post) | **POST** /rpc/SnippetService/Create | 
[**rpc_snippet_service_delete_post**](DefaultApi.md#rpc_snippet_service_delete_post) | **POST** /rpc/SnippetService/Delete | 
[**rpc_snippet_service_edit_post**](DefaultApi.md#rpc_snippet_service_edit_post) | **POST** /rpc/SnippetService/Edit | 
[**rpc_snippet_service_find_post**](DefaultApi.md#rpc_snippet_service_find_post) | **POST** /rpc/SnippetService/Find | 
[**rpc_snippet_service_list_post**](DefaultApi.md#rpc_snippet_service_list_post) | **POST** /rpc/SnippetService/List | 
[**rpc_system_service_acquire_post**](DefaultApi.md#rpc_system_service_acquire_post) | **POST** /rpc/SystemService/Acquire | 
[**rpc_system_service_boot_local_post**](DefaultApi.md#rpc_system_service_boot_local_post) | **POST** /rpc/SystemService/BootLocal | 
[**rpc_system_service_boot_network_post**](DefaultApi.md#rpc_system_service_boot_network_post) | **POST** /rpc/SystemService/BootNetwork | 
[**rpc_system_service_find_post**](DefaultApi.md#rpc_system_service_find_post) | **POST** /rpc/SystemService/Find | 
[**rpc_system_service_kickstart_post**](DefaultApi.md#rpc_system_service_kickstart_post) | **POST** /rpc/SystemService/Kickstart | 
[**rpc_system_service_list_post**](DefaultApi.md#rpc_system_service_list_post) | **POST** /rpc/SystemService/List | 
[**rpc_system_service_logs_post**](DefaultApi.md#rpc_system_service_logs_post) | **POST** /rpc/SystemService/Logs | 
[**rpc_system_service_register_post**](DefaultApi.md#rpc_system_service_register_post) | **POST** /rpc/SystemService/Register | 
[**rpc_system_service_release_post**](DefaultApi.md#rpc_system_service_release_post) | **POST** /rpc/SystemService/Release | 
[**rpc_system_service_rename_post**](DefaultApi.md#rpc_system_service_rename_post) | **POST** /rpc/SystemService/Rename | 


# **rpc_appliance_service_create_post**
> object rpc_appliance_service_create_post(appliance_service_create_request=appliance_service_create_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.appliance_service_create_request import ApplianceServiceCreateRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    appliance_service_create_request = forester_client.ApplianceServiceCreateRequest() # ApplianceServiceCreateRequest |  (optional)

    try:
        api_response = api_instance.rpc_appliance_service_create_post(appliance_service_create_request=appliance_service_create_request)
        print("The response of DefaultApi->rpc_appliance_service_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_appliance_service_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_service_create_request** | [**ApplianceServiceCreateRequest**](ApplianceServiceCreateRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_appliance_service_delete_post**
> object rpc_appliance_service_delete_post(appliance_service_delete_request=appliance_service_delete_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.appliance_service_delete_request import ApplianceServiceDeleteRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    appliance_service_delete_request = forester_client.ApplianceServiceDeleteRequest() # ApplianceServiceDeleteRequest |  (optional)

    try:
        api_response = api_instance.rpc_appliance_service_delete_post(appliance_service_delete_request=appliance_service_delete_request)
        print("The response of DefaultApi->rpc_appliance_service_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_appliance_service_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_service_delete_request** | [**ApplianceServiceDeleteRequest**](ApplianceServiceDeleteRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_appliance_service_enlist_post**
> object rpc_appliance_service_enlist_post(appliance_service_enlist_request=appliance_service_enlist_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.appliance_service_enlist_request import ApplianceServiceEnlistRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    appliance_service_enlist_request = forester_client.ApplianceServiceEnlistRequest() # ApplianceServiceEnlistRequest |  (optional)

    try:
        api_response = api_instance.rpc_appliance_service_enlist_post(appliance_service_enlist_request=appliance_service_enlist_request)
        print("The response of DefaultApi->rpc_appliance_service_enlist_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_appliance_service_enlist_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_service_enlist_request** | [**ApplianceServiceEnlistRequest**](ApplianceServiceEnlistRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_appliance_service_find_post**
> ApplianceServiceFindResponse rpc_appliance_service_find_post(appliance_service_find_request=appliance_service_find_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.appliance_service_find_request import ApplianceServiceFindRequest
from forester_client.models.appliance_service_find_response import ApplianceServiceFindResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    appliance_service_find_request = forester_client.ApplianceServiceFindRequest() # ApplianceServiceFindRequest |  (optional)

    try:
        api_response = api_instance.rpc_appliance_service_find_post(appliance_service_find_request=appliance_service_find_request)
        print("The response of DefaultApi->rpc_appliance_service_find_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_appliance_service_find_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_service_find_request** | [**ApplianceServiceFindRequest**](ApplianceServiceFindRequest.md)|  | [optional] 

### Return type

[**ApplianceServiceFindResponse**](ApplianceServiceFindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_appliance_service_list_post**
> ApplianceServiceListResponse rpc_appliance_service_list_post(appliance_service_list_request=appliance_service_list_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.appliance_service_list_request import ApplianceServiceListRequest
from forester_client.models.appliance_service_list_response import ApplianceServiceListResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    appliance_service_list_request = forester_client.ApplianceServiceListRequest() # ApplianceServiceListRequest |  (optional)

    try:
        api_response = api_instance.rpc_appliance_service_list_post(appliance_service_list_request=appliance_service_list_request)
        print("The response of DefaultApi->rpc_appliance_service_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_appliance_service_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_service_list_request** | [**ApplianceServiceListRequest**](ApplianceServiceListRequest.md)|  | [optional] 

### Return type

[**ApplianceServiceListResponse**](ApplianceServiceListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_image_service_create_post**
> ImageServiceCreateResponse rpc_image_service_create_post(image_service_create_request=image_service_create_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.image_service_create_request import ImageServiceCreateRequest
from forester_client.models.image_service_create_response import ImageServiceCreateResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    image_service_create_request = forester_client.ImageServiceCreateRequest() # ImageServiceCreateRequest |  (optional)

    try:
        api_response = api_instance.rpc_image_service_create_post(image_service_create_request=image_service_create_request)
        print("The response of DefaultApi->rpc_image_service_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_image_service_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_service_create_request** | [**ImageServiceCreateRequest**](ImageServiceCreateRequest.md)|  | [optional] 

### Return type

[**ImageServiceCreateResponse**](ImageServiceCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_image_service_delete_post**
> object rpc_image_service_delete_post(image_service_delete_request=image_service_delete_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.image_service_delete_request import ImageServiceDeleteRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    image_service_delete_request = forester_client.ImageServiceDeleteRequest() # ImageServiceDeleteRequest |  (optional)

    try:
        api_response = api_instance.rpc_image_service_delete_post(image_service_delete_request=image_service_delete_request)
        print("The response of DefaultApi->rpc_image_service_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_image_service_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_service_delete_request** | [**ImageServiceDeleteRequest**](ImageServiceDeleteRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_image_service_find_post**
> ImageServiceFindResponse rpc_image_service_find_post(image_service_find_request=image_service_find_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.image_service_find_request import ImageServiceFindRequest
from forester_client.models.image_service_find_response import ImageServiceFindResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    image_service_find_request = forester_client.ImageServiceFindRequest() # ImageServiceFindRequest |  (optional)

    try:
        api_response = api_instance.rpc_image_service_find_post(image_service_find_request=image_service_find_request)
        print("The response of DefaultApi->rpc_image_service_find_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_image_service_find_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_service_find_request** | [**ImageServiceFindRequest**](ImageServiceFindRequest.md)|  | [optional] 

### Return type

[**ImageServiceFindResponse**](ImageServiceFindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_image_service_get_by_id_post**
> ImageServiceGetByIDResponse rpc_image_service_get_by_id_post(image_service_get_by_id_request=image_service_get_by_id_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.image_service_get_by_id_request import ImageServiceGetByIDRequest
from forester_client.models.image_service_get_by_id_response import ImageServiceGetByIDResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    image_service_get_by_id_request = forester_client.ImageServiceGetByIDRequest() # ImageServiceGetByIDRequest |  (optional)

    try:
        api_response = api_instance.rpc_image_service_get_by_id_post(image_service_get_by_id_request=image_service_get_by_id_request)
        print("The response of DefaultApi->rpc_image_service_get_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_image_service_get_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_service_get_by_id_request** | [**ImageServiceGetByIDRequest**](ImageServiceGetByIDRequest.md)|  | [optional] 

### Return type

[**ImageServiceGetByIDResponse**](ImageServiceGetByIDResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_image_service_list_post**
> ImageServiceListResponse rpc_image_service_list_post(image_service_list_request=image_service_list_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.image_service_list_request import ImageServiceListRequest
from forester_client.models.image_service_list_response import ImageServiceListResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    image_service_list_request = forester_client.ImageServiceListRequest() # ImageServiceListRequest |  (optional)

    try:
        api_response = api_instance.rpc_image_service_list_post(image_service_list_request=image_service_list_request)
        print("The response of DefaultApi->rpc_image_service_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_image_service_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_service_list_request** | [**ImageServiceListRequest**](ImageServiceListRequest.md)|  | [optional] 

### Return type

[**ImageServiceListResponse**](ImageServiceListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_snippet_service_create_post**
> object rpc_snippet_service_create_post(snippet_service_create_request=snippet_service_create_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.snippet_service_create_request import SnippetServiceCreateRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    snippet_service_create_request = forester_client.SnippetServiceCreateRequest() # SnippetServiceCreateRequest |  (optional)

    try:
        api_response = api_instance.rpc_snippet_service_create_post(snippet_service_create_request=snippet_service_create_request)
        print("The response of DefaultApi->rpc_snippet_service_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_snippet_service_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_service_create_request** | [**SnippetServiceCreateRequest**](SnippetServiceCreateRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_snippet_service_delete_post**
> object rpc_snippet_service_delete_post(snippet_service_delete_request=snippet_service_delete_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.snippet_service_delete_request import SnippetServiceDeleteRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    snippet_service_delete_request = forester_client.SnippetServiceDeleteRequest() # SnippetServiceDeleteRequest |  (optional)

    try:
        api_response = api_instance.rpc_snippet_service_delete_post(snippet_service_delete_request=snippet_service_delete_request)
        print("The response of DefaultApi->rpc_snippet_service_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_snippet_service_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_service_delete_request** | [**SnippetServiceDeleteRequest**](SnippetServiceDeleteRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_snippet_service_edit_post**
> object rpc_snippet_service_edit_post(snippet_service_edit_request=snippet_service_edit_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.snippet_service_edit_request import SnippetServiceEditRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    snippet_service_edit_request = forester_client.SnippetServiceEditRequest() # SnippetServiceEditRequest |  (optional)

    try:
        api_response = api_instance.rpc_snippet_service_edit_post(snippet_service_edit_request=snippet_service_edit_request)
        print("The response of DefaultApi->rpc_snippet_service_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_snippet_service_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_service_edit_request** | [**SnippetServiceEditRequest**](SnippetServiceEditRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_snippet_service_find_post**
> SnippetServiceFindResponse rpc_snippet_service_find_post(snippet_service_find_request=snippet_service_find_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.snippet_service_find_request import SnippetServiceFindRequest
from forester_client.models.snippet_service_find_response import SnippetServiceFindResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    snippet_service_find_request = forester_client.SnippetServiceFindRequest() # SnippetServiceFindRequest |  (optional)

    try:
        api_response = api_instance.rpc_snippet_service_find_post(snippet_service_find_request=snippet_service_find_request)
        print("The response of DefaultApi->rpc_snippet_service_find_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_snippet_service_find_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_service_find_request** | [**SnippetServiceFindRequest**](SnippetServiceFindRequest.md)|  | [optional] 

### Return type

[**SnippetServiceFindResponse**](SnippetServiceFindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_snippet_service_list_post**
> SnippetServiceListResponse rpc_snippet_service_list_post(snippet_service_list_request=snippet_service_list_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.snippet_service_list_request import SnippetServiceListRequest
from forester_client.models.snippet_service_list_response import SnippetServiceListResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    snippet_service_list_request = forester_client.SnippetServiceListRequest() # SnippetServiceListRequest |  (optional)

    try:
        api_response = api_instance.rpc_snippet_service_list_post(snippet_service_list_request=snippet_service_list_request)
        print("The response of DefaultApi->rpc_snippet_service_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_snippet_service_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_service_list_request** | [**SnippetServiceListRequest**](SnippetServiceListRequest.md)|  | [optional] 

### Return type

[**SnippetServiceListResponse**](SnippetServiceListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_acquire_post**
> object rpc_system_service_acquire_post(system_service_acquire_request=system_service_acquire_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_acquire_request import SystemServiceAcquireRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_acquire_request = forester_client.SystemServiceAcquireRequest() # SystemServiceAcquireRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_acquire_post(system_service_acquire_request=system_service_acquire_request)
        print("The response of DefaultApi->rpc_system_service_acquire_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_acquire_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_acquire_request** | [**SystemServiceAcquireRequest**](SystemServiceAcquireRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_boot_local_post**
> object rpc_system_service_boot_local_post(system_service_boot_local_request=system_service_boot_local_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_boot_local_request import SystemServiceBootLocalRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_boot_local_request = forester_client.SystemServiceBootLocalRequest() # SystemServiceBootLocalRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_boot_local_post(system_service_boot_local_request=system_service_boot_local_request)
        print("The response of DefaultApi->rpc_system_service_boot_local_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_boot_local_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_boot_local_request** | [**SystemServiceBootLocalRequest**](SystemServiceBootLocalRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_boot_network_post**
> object rpc_system_service_boot_network_post(system_service_boot_network_request=system_service_boot_network_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_boot_network_request import SystemServiceBootNetworkRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_boot_network_request = forester_client.SystemServiceBootNetworkRequest() # SystemServiceBootNetworkRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_boot_network_post(system_service_boot_network_request=system_service_boot_network_request)
        print("The response of DefaultApi->rpc_system_service_boot_network_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_boot_network_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_boot_network_request** | [**SystemServiceBootNetworkRequest**](SystemServiceBootNetworkRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_find_post**
> SystemServiceFindResponse rpc_system_service_find_post(system_service_find_request=system_service_find_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_find_request import SystemServiceFindRequest
from forester_client.models.system_service_find_response import SystemServiceFindResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_find_request = forester_client.SystemServiceFindRequest() # SystemServiceFindRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_find_post(system_service_find_request=system_service_find_request)
        print("The response of DefaultApi->rpc_system_service_find_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_find_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_find_request** | [**SystemServiceFindRequest**](SystemServiceFindRequest.md)|  | [optional] 

### Return type

[**SystemServiceFindResponse**](SystemServiceFindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_kickstart_post**
> SystemServiceKickstartResponse rpc_system_service_kickstart_post(system_service_kickstart_request=system_service_kickstart_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_kickstart_request import SystemServiceKickstartRequest
from forester_client.models.system_service_kickstart_response import SystemServiceKickstartResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_kickstart_request = forester_client.SystemServiceKickstartRequest() # SystemServiceKickstartRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_kickstart_post(system_service_kickstart_request=system_service_kickstart_request)
        print("The response of DefaultApi->rpc_system_service_kickstart_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_kickstart_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_kickstart_request** | [**SystemServiceKickstartRequest**](SystemServiceKickstartRequest.md)|  | [optional] 

### Return type

[**SystemServiceKickstartResponse**](SystemServiceKickstartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_list_post**
> SystemServiceListResponse rpc_system_service_list_post(system_service_list_request=system_service_list_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_list_request import SystemServiceListRequest
from forester_client.models.system_service_list_response import SystemServiceListResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_list_request = forester_client.SystemServiceListRequest() # SystemServiceListRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_list_post(system_service_list_request=system_service_list_request)
        print("The response of DefaultApi->rpc_system_service_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_list_request** | [**SystemServiceListRequest**](SystemServiceListRequest.md)|  | [optional] 

### Return type

[**SystemServiceListResponse**](SystemServiceListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_logs_post**
> SystemServiceLogsResponse rpc_system_service_logs_post(system_service_logs_request=system_service_logs_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_logs_request import SystemServiceLogsRequest
from forester_client.models.system_service_logs_response import SystemServiceLogsResponse
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_logs_request = forester_client.SystemServiceLogsRequest() # SystemServiceLogsRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_logs_post(system_service_logs_request=system_service_logs_request)
        print("The response of DefaultApi->rpc_system_service_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_logs_request** | [**SystemServiceLogsRequest**](SystemServiceLogsRequest.md)|  | [optional] 

### Return type

[**SystemServiceLogsResponse**](SystemServiceLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_register_post**
> object rpc_system_service_register_post(system_service_register_request=system_service_register_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_register_request import SystemServiceRegisterRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_register_request = forester_client.SystemServiceRegisterRequest() # SystemServiceRegisterRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_register_post(system_service_register_request=system_service_register_request)
        print("The response of DefaultApi->rpc_system_service_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_register_request** | [**SystemServiceRegisterRequest**](SystemServiceRegisterRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_release_post**
> object rpc_system_service_release_post(system_service_release_request=system_service_release_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_release_request import SystemServiceReleaseRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_release_request = forester_client.SystemServiceReleaseRequest() # SystemServiceReleaseRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_release_post(system_service_release_request=system_service_release_request)
        print("The response of DefaultApi->rpc_system_service_release_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_release_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_release_request** | [**SystemServiceReleaseRequest**](SystemServiceReleaseRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rpc_system_service_rename_post**
> object rpc_system_service_rename_post(system_service_rename_request=system_service_rename_request)



### Example


```python
import time
import os
import forester_client
from forester_client.models.system_service_rename_request import SystemServiceRenameRequest
from forester_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://forester.example.com:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = forester_client.Configuration(
    host = "https://forester.example.com:8000"
)


# Enter a context with an instance of the API client
with forester_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = forester_client.DefaultApi(api_client)
    system_service_rename_request = forester_client.SystemServiceRenameRequest() # SystemServiceRenameRequest |  (optional)

    try:
        api_response = api_instance.rpc_system_service_rename_post(system_service_rename_request=system_service_rename_request)
        print("The response of DefaultApi->rpc_system_service_rename_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rpc_system_service_rename_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_service_rename_request** | [**SystemServiceRenameRequest**](SystemServiceRenameRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Client error |  -  |
**5XX** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

