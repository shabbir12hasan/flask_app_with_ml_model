ifndef WORKSPACE
	WORKSPACE := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../..)
endif
SRC_DIR := $(WORKSPACE)/src

TRAINING_APP_IMAGE = training-app
TRAINING_APP_CONTAINER = training-app-container
SBR_ENV=Prd
CAREABOUT_HOME=/opt

# ENV=tst
HOME=/opt

help:
	@echo "-------------- available commands: ----------------------------------"
	@echo "make build-string-detector         - build string detector default"

build-string-detector:
	@echo "start"
	# @echo SRC_DIR
	# $(info   path: $(PATH))
	# $(info   PROJECT_DIR: $(PROJECT_DIR))
	@echo "build string-detector"
	@docker-compose build string_detector

echo-env:
	@echo ""
	@env

.EXPORT_ALL_VARIABLES:
