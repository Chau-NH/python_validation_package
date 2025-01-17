
from .exceptions import ValidationError

class Validator:
    @staticmethod
    def validate_type(value, expected_type):
        if  value is not None and not isinstance(value, expected_type):
            raise ValidationError(f"Expected type is {expected_type.__name__} but got {type(value).__name__}.")
        
    @staticmethod
    def validate_range(value, min_value=None, max_value=None):
        if min_value is not None and value < min_value:
            raise ValidationError(f"Value {value} is less than minimum allowed {min_value}.")
        if max_value is not None and value > max_value:
            raise ValidationError(f"Value {value} is greater than maximum allowed {max_value}.")
        
    @staticmethod
    def validate_length(value, min_length=None, max_length=None):
        if not hasattr(value, "__len__"):
            raise ValidationError("Value has no length attribute to validate")
        length = len(value)
        if min_length is not None and length < min_length:
            raise ValidationError(f"Length {length} is less than minimum allowed {min_length}.")
        if max_length is not None and length > max_length:
            raise ValidationError(f"Length {length} is greater than maximum allowed {max_length}.")
    
    @staticmethod
    def validate_choices(value, choices):
        if value not in choices:
            raise ValidationError(f"Value {value} is not in allowed choices: {choices}.")
        
    @staticmethod
    def validate_pattern(value, pattern):
        import re
        if not re.match(pattern, value):
            raise ValidationError(f"Value {value} does not match pattern: {pattern}.")
        
    @staticmethod
    def validate_required(value):
        if value is None:
            raise ValidationError(f"This field is required and can not be None")
        
    @staticmethod
    def validate_uploaded_file(file_object, allowed_extensions=None, max_size=None):
        if file_object is None:
            raise ValidationError(f"No file uploaded.")
        
        file_name = getattr(file_object, 'filename', getattr(file_object, 'name', None))
        if not file_name:
            raise ValidationError(f"Unable to determine the file name.")

        if allowed_extensions:
            if not any(file_name.lower().endswith(ext.lower()) for ext in allowed_extensions):
                raise ValidationError(f"Invalid file extension. Allowed extensions are: {', '.join(allowed_extensions)}")

        if max_size:
            file_object.seek(0, 2)
            file_size = file_object.tell()
            file_object.seek(0)
            if file_size > max_size:
                raise ValidationError(
                    f"File size exceeds the maximum limit of {max_size} bytes. Uploaded file size: {file_size} bytes."
                )
