# Validation Package 

This is a Validation Package

## Installation

### On TestPyPi

```bash
pip install -i https://test.pypi.org/simple/ validation_package_cn
```

### On Local
```bash
pip install .
```

## Example Usage
```python
if __name__ == "__main__":
    schema = {
        "age": {"type": int, "max": 120, "min": 0, "required": True},
        "name": {"type": str, "min_length": 3, "required": True},
        "email": {"type": str, "pattern": r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$", "required": True},
        "status": {"type": str, "choices": ["active", "inactive"], "required": True},
        "uploaded_file": {"uploaded_file": {"allowed_extensions": [".pdf", ".docx"], "max_size": 2097152}, "required": True},
    }

    data = {
        "age": 25,
        "name": "johndoe",
        "email": "johndoe@example.com",
        "status": "active",
        "uploaded_file": open("requirements.txt", "rb")
    }

    validator = SchemaValidator(schema)

    try:
        validator.validate(data)
        print("Validation successful!")
    except ValidationError as e:
        print("Validation errors:", e)
```