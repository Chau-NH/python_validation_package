from datetime import datetime
from src.validation_package_cn import ValidationException, SchemaValidator, validator

if __name__ == "__main__":
    schema = {
        "age": {"type": int, "lte": 120, "gte": 0, "required": True},
        "name": {"type": str, "min_length": 3, "required": True},
        "email": {"type": str, "regex": r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$", "required": True},
        "status": {"type": str, "in": ["active", "inactive"], "required": True},
        "uploaded_file": {"required": True, "file_extension": [".pdf", ".docx", ".txt"]},
        "event_date": {"datetime": {"format": "%Y-%m-%d %H:%M:%S", "before_or_equals": "2025-12-31 00:00:00"}}
    }

    data = {
        "age": 25,
        "name": "johndoe",
        "email": "johndoe@example.com",
        "status": "active",
        "uploaded_file": open("requirements.txt", "rb"),
        "event_date": "2026-01-01 00:00:00"
    }

    validator = SchemaValidator(schema)

    try:
        validator.validate(data)
        print("Validation successful!")
    except ValidationException as e:
        print("Validation errors:", e)
