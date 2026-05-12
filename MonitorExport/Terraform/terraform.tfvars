output "lambda_arn" {
  value = aws_lambda_function.monitor_export.arn
}
 
aws_region = "us-east-1"
 
sender_email = "kiransubagan@gmail.com"
 
receiver_email = "kiransubhagan85@gmail.com"
 
