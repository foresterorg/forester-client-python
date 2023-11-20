# coding: utf-8

"""
    ImageService API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from forester-client.models.error_webrpc_bad_response import ErrorWebrpcBadResponse
from forester-client.models.error_webrpc_internal_error import ErrorWebrpcInternalError
from forester-client.models.error_webrpc_server_panic import ErrorWebrpcServerPanic
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

RPCIMAGESERVICECREATEPOST5XXRESPONSE_ONE_OF_SCHEMAS = ["ErrorWebrpcBadResponse", "ErrorWebrpcInternalError", "ErrorWebrpcServerPanic"]

class RpcImageServiceCreatePost5XXResponse(BaseModel):
    """
    RpcImageServiceCreatePost5XXResponse
    """
    # data type: ErrorWebrpcBadResponse
    oneof_schema_1_validator: Optional[ErrorWebrpcBadResponse] = None
    # data type: ErrorWebrpcServerPanic
    oneof_schema_2_validator: Optional[ErrorWebrpcServerPanic] = None
    # data type: ErrorWebrpcInternalError
    oneof_schema_3_validator: Optional[ErrorWebrpcInternalError] = None
    actual_instance: Optional[Union[ErrorWebrpcBadResponse, ErrorWebrpcInternalError, ErrorWebrpcServerPanic]] = None
    one_of_schemas: List[str] = Literal["ErrorWebrpcBadResponse", "ErrorWebrpcInternalError", "ErrorWebrpcServerPanic"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = RpcImageServiceCreatePost5XXResponse.model_construct()
        error_messages = []
        match = 0
        # validate data type: ErrorWebrpcBadResponse
        if not isinstance(v, ErrorWebrpcBadResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ErrorWebrpcBadResponse`")
        else:
            match += 1
        # validate data type: ErrorWebrpcServerPanic
        if not isinstance(v, ErrorWebrpcServerPanic):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ErrorWebrpcServerPanic`")
        else:
            match += 1
        # validate data type: ErrorWebrpcInternalError
        if not isinstance(v, ErrorWebrpcInternalError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ErrorWebrpcInternalError`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in RpcImageServiceCreatePost5XXResponse with oneOf schemas: ErrorWebrpcBadResponse, ErrorWebrpcInternalError, ErrorWebrpcServerPanic. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in RpcImageServiceCreatePost5XXResponse with oneOf schemas: ErrorWebrpcBadResponse, ErrorWebrpcInternalError, ErrorWebrpcServerPanic. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ErrorWebrpcBadResponse
        try:
            instance.actual_instance = ErrorWebrpcBadResponse.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ErrorWebrpcServerPanic
        try:
            instance.actual_instance = ErrorWebrpcServerPanic.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ErrorWebrpcInternalError
        try:
            instance.actual_instance = ErrorWebrpcInternalError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RpcImageServiceCreatePost5XXResponse with oneOf schemas: ErrorWebrpcBadResponse, ErrorWebrpcInternalError, ErrorWebrpcServerPanic. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RpcImageServiceCreatePost5XXResponse with oneOf schemas: ErrorWebrpcBadResponse, ErrorWebrpcInternalError, ErrorWebrpcServerPanic. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


