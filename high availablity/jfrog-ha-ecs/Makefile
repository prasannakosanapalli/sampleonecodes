.PHONY: help run submodules

submodules:
	git submodule init
	git submodule update
	cd submodules/quickstart-linux-bastion && git submodule init && git submodule update 
	cd submodules/quickstart-amazon-eks && git submodule init && git submodule update 

help:
	@echo   "make test  : executes taskcat"

create:
	aws cloudformation create-stack --stack-name jfrog-ecs --template-body file://ecs.yaml

validate:
	aws cloudformation validate-template --template-body file://ecs.yaml

delete:
	aws cloudformation delete-stack --stack-name jfrog-ecs

.ONESHELL:
test: lint submodules
	cd .. && pwd && taskcat -c theflash/ci/config.yml -n

lint:
	time taskcat -l -c ci/config.yml


