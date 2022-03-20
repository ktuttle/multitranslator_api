import boto3

from app import translate_text

translate_client = boto3.client('translate')


def lambda_handler(event, context):
    # if event["headers"]["Api-Key"] != 'abc123':
    #     return {"statusCode": 401}

    source_text = event["queryStringParameters"]["source_text"]
    lang_codes = event["queryStringParameters"]["lang_codes"].split(",")

    translated_text_data = translate_text(
        source_text=source_text,
        lang_codes=lang_codes,
        translate_client=translate_client,
    )

    return translated_text_data
