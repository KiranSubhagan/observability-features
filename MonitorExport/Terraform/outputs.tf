variable "aws_region" {
  default = "us-east-1"
}
 
variable "lambda_name" {
  default = "monitor-export"
}

output "lambda_arn" {
  value = aws_lambda_function.monitor_export.arn
}
 
variable "sender_email" {}
 
variable "receiver_email" {}
