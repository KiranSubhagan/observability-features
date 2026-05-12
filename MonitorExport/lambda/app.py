import os
import csv
import io
import boto3
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
 
ses = boto3.client("ses")
 
SENDER = os.environ["SENDER_EMAIL"]
RECEIVER = os.environ["RECEIVER_EMAIL"]
 
 
def lambda_handler(event, context):
 
    monitors = event.get("monitors", [])
 
    csv_buffer = io.StringIO()
 
    writer = csv.writer(csv_buffer)
 
    writer.writerow([
        "id",
        "name",
        "type"
    ])
 
    for monitor in monitors:
 
        writer.writerow([
            monitor.get("id"),
            monitor.get("name"),
            monitor.get("type")
        ])
 
    csv_content = csv_buffer.getvalue()
 
    msg = MIMEMultipart()
 
    msg["Subject"] = "Datadog Monitor Export"
 
    msg["From"] = SENDER
 
    msg["To"] = RECEIVER
 
    body = MIMEText(
        "Attached is the Datadog monitor export CSV."
    )
 
    msg.attach(body)
 
    attachment = MIMEBase(
        "application",
        "octet-stream"
    )
 
    attachment.set_payload(csv_content)
 
    encoders.encode_base64(attachment)
 
    attachment.add_header(
        "Content-Disposition",
        "attachment",
        filename="monitors.csv"
    )
 
    msg.attach(attachment)
 
    ses.send_raw_email(
        Source=SENDER,
 
        Destinations=[
            RECEIVER
        ],
 
        RawMessage={
            "Data": msg.as_string()
        }
    )
 
    return {
        "status": "success",
        "monitor_count": len(monitors)
    }
