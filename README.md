# Validation Package 

This is a Validation Package

## Installation

```bash
pip install -i https://test.pypi.org/simple/ validation_package_cn
```

## Example Usage
```python
if __name__ == "__main__":
    schema = {
        "age": {"type": int, "range": (0, 120)},
        "name": {"type": str, "length": (1, 50)},
        "email": {"type": str, "pattern": r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$"},
        "status": {"type": str, "choices": ["active", "inactive"]},
    }

    data = {
        "age": 25,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "status": "active",
    }

    validator = SchemaValidator(schema)

    try:
        validator.validate(data)
        print("Validation successful!")
    except ValidationError as e:
        print("Validation errors:", e)
```