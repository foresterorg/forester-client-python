#!/bin/bash

# Use generateSourceCodeOnly option to regenerate metadata files.

podman run --rm \
	--volume "$PWD":/w:Z \
	docker.io/openapitools/openapi-generator-cli generate \
	--generator-name python \
	--input-spec 'https://raw.githubusercontent.com/foresterorg/forester/main/openapi.gen.yaml' \
	--output /w \
	--package-name forester-client \
	--global-property=models,supportingFiles,apis,apiDocs=true,modelDocs=false,apiTests=false,modelTests=false \
	--additional-properties=generateSourceCodeOnly=false,packageVersion=0.0.1,packageUrl=https://github.com/foresterorg/forester-client-python
