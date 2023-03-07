resource "google_project_iam_member" "iam_workflows_invoker" {
  project = var.project
  role    = "roles/workflows.invoker"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}

resource "google_project_iam_member" "iam_cloudfunctions_invoker" {
  project = var.project
  role    = "roles/cloudfunctions.invoker"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}

resource "google_project_iam_member" "iam_logging_logwriter" {
  project = var.project
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.service_account.email}"
}
