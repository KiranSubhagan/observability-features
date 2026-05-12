resource "aws_lambda_function" "monitor_export" {
 
  function_name = var.lambda_name
 
  role = aws_iam_role.lambda_role.arn
 
  runtime = "python3.12"
 
  handler = "app.lambda_handler"
 
  filename         = "../lambda/lambda.zip"
  source_code_hash = filebase64sha256("../lambda/lambda.zip")
 
  timeout = 30
 
  environment {
    variables = {
      SENDER_EMAIL   = var.sender_email
      RECEIVER_EMAIL = var.receiver_email
    }
  }
}
