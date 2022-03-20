def translate_text(
    source_text: str,
    lang_codes: list[str],
    translate_client,
):
    translated_text_data = {}

    for lang_code in lang_codes:
        response = translate_client.translate_text(
            Text=source_text,
            SourceLanguageCode="en",
            TargetLanguageCode=lang_code,
        )

        translated_text_data[lang_code] = response["TranslatedText"]

    return translated_text_data
