init:
	terraform init \
		-backend-config=bucket=terraform_$(PROJECT_ID) \
		-backend-config=prefix=workflow-job-wrapper

plan:
	terraform plan -var "project=$(PROJECT_ID)"

apply:
	terraform apply -var "project=$(PROJECT_ID)"

docs:
	terraform-docs -c .tfdocs-config.yaml .

format:
	terraform fmt -recursive
