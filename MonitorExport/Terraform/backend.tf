terraform {
  backend "s3" {
    bucket         = "ecs-demo-terraform-state"
    key            = "datadog/dev/terraform.tfstate"
    region         = "ap-south-1"
  }
}
