# Provision the Service Account with permission to invoke a Workflow (includes permission to POST to the 'callback' URL)
resource "google_project_iam_member" "iam_workflows_invoker" {
  project = var.project
  role    = "roles/workflows.invoker"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}

# Provision the Service Account with permission to publish to Pub/Sub (the 'Job')
resource "google_project_iam_member" "iam_pubsub_publisher" {
  project = var.project
  role    = "roles/pubsub.publisher"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}

# Provision the Service Account with permission to write logs
resource "google_project_iam_member" "iam_logging_logwriter" {
  project = var.project
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}
