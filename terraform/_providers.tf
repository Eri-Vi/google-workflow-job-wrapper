# Configure the Google Cloud provider
provider "google" {
  project = var.project
  region  = "australia-southeast1"
}

provider "archive" {
}

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.50.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "2.3.0"
    }
  }

  backend "gcs" {
  }
}
