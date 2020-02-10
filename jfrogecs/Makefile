help:
	@echo   "make test  : executes taskcat"

create:
	aws cloudformation create-stack --stack-name test --template-body file://monday.yaml

validate: 
    
	aws cloudformation validate-template --template-body file://monday.yaml
update:
    
	aws cloudformation update-stack --stack-name test --template-body file://monday.yaml

delete:
	aws cloudformation delete-stack --stack-name test
