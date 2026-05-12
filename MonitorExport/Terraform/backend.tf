terraform {
  backend "s3" {
    bucket         = "ecs-demo-terraform-state"
    key            = "datadog/dev/terraform_monitor_export.tfstate"
    region         = "ap-south-1"
  }
}
