import boto3
from botocore.exceptions import ClientError
import os
import datetime
import smtplib

S_email = "&&&&&&&&&&&&&"
S_pass = "**********"
to_address = "**********"



def upload_file_to_s3(file_name, bucket):
    today = datetime.datetime.now()
    year = str(today.year)
    month = str(today.month)

    object_name = year + "/" + month + "/" + os.path.basename(file_name)
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == '__main__':
    path = "/Users/queenasong/PycharmProjects/Loeb-project/loab-data-file/"
    files = os.listdir(path=path)
    for file in files:
        upload_file_to_s3(path+file,"loeb-financial-data")


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(S_email,S_pass)
        connection.sendmail(from_addr=S_email,to_addrs=to_address,
                                msg="Today's report has been uploaded.\n\nPlease check the loeb-financial-data bucket.")
        connection.quit()
        print(f"Successfully send email to {to_address}.")

