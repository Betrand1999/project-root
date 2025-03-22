
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import boto3

def get_videos():
    from settings import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY
    print(AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY)
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )
    bucket_name = 'my-doc-betrand'
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    videos = []
    if 'Contents' in response:
        for obj in response['Contents']:
            
            obj_key = str(obj['Key'])
            if obj_key.endswith(".mp4"):
                object_url = s3_client.generate_presigned_url('get_object',
                                                Params={'Bucket': bucket_name, 'Key': obj_key},
                                                ExpiresIn=3600)
                videos.append(object_url)
        return videos
    else:
        print("Bucket is empty or does not exist.")
        return None
               
    # return ["https://my-doc-betrand.s3.amazonaws.com/1.mp4", "https://my-doc-betrand.s3.amazonaws.com/2.mp4", "https://my-doc-betrand.s3.amazonaws"]

def send_email(subject, recipient, body):
    from settings import EMAIL_PASS, EMAIL_USER, SMTP_PORT, SMTP_SERVER
    sender_email = EMAIL_USER
    sender_password = EMAIL_PASS
    smtp_server =SMTP_SERVER
    smtp_port = SMTP_PORT

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")