init:
	terraform init \
		-backend-config=bucket=terraform_erika-dev \
		-backend-config=prefix=workflow-job-wrapper

plan:
	terraform plan -var "project=$(PROJECT_ID)"
