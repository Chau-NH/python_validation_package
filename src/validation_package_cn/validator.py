
from .exceptions import ValidationError

class Validator:
    @staticmethod
    def validate_type(field, value, expected_type):
        if not isinstance(value, expected_type):
            raise ValidationError(f"Expected type of {field} is {expected_type.__name__} but got {type(value).__name__}.")
        
    @staticmethod
    def validate_range(field, value, min_value=None, max_value=None):
        if min_value is not None and value < min_value:
            raise ValidationError(f"Value {value} of {field} is less than minimum allowed {min_value}.")
        if max_value is not None and value > max_value:
            raise ValidationError(f"Value {value} of {field} is greater than maximum allowed {max_value}.")
        
    @staticmethod
    def validate_length(field, value, min_length=None, max_length=None):
        if not hasattr(value, "__len__"):
            raise ValidationError("Value of {field} has no length attribute to validate")
        length = len(value)
        if min_length is not None and length < min_length:
            raise ValidationError(f"Length {length} of {field} is less than minimum allowed {min_length}.")
        if max_length is not None and length > max_length:
            raise ValidationError(f"Length {length} of {field} is greater than maximum allowed {max_length}.")
    
    @staticmethod
    def validate_choices(field, value, choices):
        if value not in choices:
            raise ValidationError(f"Value {value} of {field} is not in allowed choices: {choices}.")
        
    @staticmethod
    def validate_pattern(field, value, pattern):
        import re
        if not re.match(pattern, value):
            raise ValidationError(f"Value {value} of {field} does not match pattern: {pattern}.")
        
    @staticmethod
    def validate_required(field, value):
        if value is None:
            raise ValidationError(f"FIeld {field} is required and can not be None")

