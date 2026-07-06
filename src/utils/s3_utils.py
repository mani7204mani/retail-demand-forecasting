import boto3
from botocore.exceptions import ClientError
from datetime import datetime
BUCKET_NAME = "retail-demand-forecasting-mani"

s3 = boto3.client("s3")


def upload_prediction_history(file_path):
    try:
        s3_key = f"prediction-history/prediction_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        s3.upload_file(
            file_path,
            BUCKET_NAME,
            s3_key
        )
        return True

    except ClientError as e:
        print(e)
        return False