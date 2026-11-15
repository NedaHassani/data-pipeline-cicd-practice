def clean_record(record: dict) -> dict:
    """Normalize one raw record from an API."""
    return {
        "id" : int(record["id"]),
        "name" : record["name"].strip().title(),
    }