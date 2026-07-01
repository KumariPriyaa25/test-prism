terraform {
  required_version = ">= 1.5.0"
}

provider "local" {}

resource "local_file" "example" {
  filename = "${path.module}/terraform-output.txt"
  content  = "Hello from Terraform"
}