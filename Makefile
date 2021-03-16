SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

PWD := $(shell pwd)
TEST_FILTER ?= ""
TEST_MARKERS ?= "not minio and not gcs"

S3DIR := ${PWD}/tmp-data


first: help

.PHONY: clean
clean:  ## Clean build files


.PHONY: help
help:  ## Show this help menu
	@grep -E '^[0-9a-zA-Z_-]+:.*?##.*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?##"; OFS="\t\t"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, ($$2==""?"":$$2)}'


# ------------------------------------------------------------------------------

kafka:  ## Download kafka
	curl -O https://www.apache.org/dyn/closer.cgi?path=/kafka/2.7.0/kafka_2.13-2.7.0.tgz
	tar -zxvf kafka_2.13-2.7.0.tgz
	rm kafka_2.13-2.7.0.tgz
	mv kafka_* kafka
