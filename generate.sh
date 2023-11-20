#!/bin/bash

# Use .openapi-generator-ignore to ignore files!

podman run --rm \
	--volume "$PWD":/w:Z \
	docker.io/openapitools/openapi-generator-cli generate \
	--generator-name python \
	--input-spec 'https://raw.githubusercontent.com/foresterorg/forester/main/openapi.gen.yaml' \
	--output /w \
	--package-name forester_client \
	--additional-properties=packageVersion=0.0.1,packageUrl=https://github.com/foresterorg/forester-client-python
