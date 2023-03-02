data "archive_file" "job_code" {
  type        = "zip"
  source_dir  = "${path.module}/../job"
  output_path = "job.zip"
}

resource "google_storage_bucket" "code_artifacts" {
  name          = "code-artifacts_${var.project}"
  location      = "australia-southeast1"
  force_destroy = true

  uniform_bucket_level_access = true
}

resource "google_storage_bucket_object" "job_code" {
  name   = "job_code_${data.archive_file.job_code.output_sha}.zip"
  source = data.archive_file.job_code.output_path
  bucket = google_storage_bucket.code_artifacts.id
}

# Create a Pub/Sub topic
resource "google_pubsub_topic" "mock_job_topic" {
  name = "mock-job-topic"
}

# Create a Cloud Function
resource "google_cloudfunctions_function" "mock_job_service" {
  name        = "mock-job-service"
  runtime     = "python311"

  # Set the entry point for the function
  entry_point = "process_event"

  # Define the function's source code
  source_archive_bucket = google_storage_bucket.code_artifacts.name
  source_archive_object = google_storage_bucket_object.job_code.name

  # Configure the function to be triggered by the Pub/Sub topic
  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = google_pubsub_topic.mock_job_topic.id
  }
}

# Create a Cloud Workflow
resource "google_workflows_workflow" "example_workflow" {
  name        = "job-wrapper"
  region      = "australia-southeast1"
  source_contents = templatefile("../workflow/job-wrapper.yaml", {topic_id = google_pubsub_topic.mock_job_topic.id})
}
