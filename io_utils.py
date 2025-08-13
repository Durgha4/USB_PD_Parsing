import json

def save_jsonl(data, path):
    """Save list of dicts to a JSONL file."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            for record in data:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception as e:
        raise RuntimeError(f"Error saving {path}: {e}")

def validate_json(data, schema):
    """Validate a dict against JSON schema."""
    from jsonschema import validate, ValidationError
    try:
        validate(data, schema)
        return True
    except ValidationError as err:
        raise ValueError(f"Schema validation error: {err.message}")
