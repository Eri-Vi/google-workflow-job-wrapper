<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_archive"></a> [archive](#requirement\_archive) | 2.3.0 |
| <a name="requirement_google"></a> [google](#requirement\_google) | 4.50.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_archive"></a> [archive](#provider\_archive) | 2.3.0 |
| <a name="provider_google"></a> [google](#provider\_google) | 4.50.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [google_cloudfunctions_function.mock_job_service](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/cloudfunctions_function) | resource |
| [google_project_iam_member.iam_cloudfunctions_invoker](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/project_iam_member) | resource |
| [google_project_iam_member.iam_logging_logwriter](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/project_iam_member) | resource |
| [google_project_iam_member.iam_workflows_invoker](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/project_iam_member) | resource |
| [google_pubsub_topic.mock_job_topic](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/pubsub_topic) | resource |
| [google_service_account.service_account](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/service_account) | resource |
| [google_storage_bucket.code_artifacts](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/storage_bucket) | resource |
| [google_storage_bucket_object.job_code](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/storage_bucket_object) | resource |
| [google_workflows_workflow.example_workflow](https://registry.terraform.io/providers/hashicorp/google/4.50.0/docs/resources/workflows_workflow) | resource |
| [archive_file.job_code](https://registry.terraform.io/providers/hashicorp/archive/2.3.0/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_project"></a> [project](#input\_project) | Google project in which to deploy resources. | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END_TF_DOCS -->