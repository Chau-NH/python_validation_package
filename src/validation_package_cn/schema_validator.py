from .exceptions import ValidationError
from .validator import Validator

validators = {
    "required": lambda value, rule: Validator.validate_required(value),
    "type": lambda value, rule: Validator.validate_type(value, rule),
    "min": lambda value, rule: Validator.validate_range(value, min_value=rule),
    "max": lambda value, rule: Validator.validate_range(value, max_value=rule),
    "min_length": lambda value, rule: Validator.validate_length(value, min_length=rule),
    "max_length": lambda value, rule: Validator.validate_length(value, max_length=rule),
    "choices": lambda value, rule: Validator.validate_choices(value, rule),
    "pattern": lambda value, rule: Validator.validate_pattern(value, rule),
    "uploaded_file": lambda value, rule: Validator.validate_uploaded_file(value, **rule),
}
class SchemaValidator:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        errors = {}
        for field, rules in self.schema.items():
            value = data.get(field)
            try:
                for rule_name, rule_value in rules.items():
                    if rule_name in validators:
                        validators[rule_name](value, rule_value)

            except ValidationError as e:
                errors[field] = str(e)
        
        if errors:
            raise ValidationError(errors)
