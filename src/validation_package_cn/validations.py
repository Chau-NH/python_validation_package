import io, re
from datetime import datetime
from .validation_exception import ValidationException

def validate_type(value, expected_type):
    if  value is not None and not isinstance(value, expected_type):
        raise ValidationException(f"Expected type is {expected_type.__name__} but got {type(value).__name__}.")
    
def validate_gt(value, threshold):
    if value is not None and value <= threshold:
        raise ValidationException(f"Value {value} must be greater than {threshold}.")

def validate_lt(value, threshold):
    if value is not None and value >= threshold:
        raise ValidationException(f"Value {value} must be less than {threshold}.")

def validate_gte(value, threshold):
    if value is not None and value < threshold:
        raise ValidationException(f"Value {value} must be greater than or equal to {threshold}.")

def validate_lte(value, threshold):
    if value is not None and value > threshold:
        raise ValidationException(f"Value {value} must be less than or equal to {threshold}.")
            
def validate_min_length(value, min_length):
    if value is not None and hasattr(value, "__len__") and len(value) < min_length:
        raise ValidationException(f"Length {len(value)} is less than minimum allowed {min_length}.")

def validate_max_length(value, max_length):
    if value is not None and hasattr(value, "__len__") and len(value) > max_length:
        raise ValidationException(f"Length {len(value)} is greater than maximum allowed {max_length}.")

def validate_in(value, choices):
    if value not in choices:
        raise ValidationException(f"Value {value} is not in allowed choices: {choices}.")

def validate_not_in(value, choices):
    if value in choices:
        raise ValidationException(f"Value {value} is in forbidden choices: {choices}.")
    
def validate_regex(value, pattern):
    if not re.match(pattern, value):
        raise ValidationException(f"Value {value} does not match pattern: {pattern}.")
    
def validate_required(value, required = True):
    if required and value is None:
        raise ValidationException(f"This field is required and can not be None")
    
def validate_file_extension(file_object, allowed_extensions=None):
    if file_object is not None and isinstance(file_object, (io.IOBase)):
        file_name = getattr(file_object, 'filename', getattr(file_object, 'name', None))
        if not file_name:
            raise ValidationException(f"Unable to determine the file name.")

        if allowed_extensions:
            if not any(file_name.lower().endswith(ext.lower()) for ext in allowed_extensions):
                raise ValidationException(f"Invalid file extension. Allowed extensions are: {', '.join(allowed_extensions)}")
    else:
        raise ValidationException("Invalid file object provided.")

def validate_max_size(file_object, max_size):
    if file_object is not None and isinstance(file_object, (io.IOBase)):
        
        """Validate that an uploaded file does not exceed the max size (in bytes)."""
        file_object.seek(0, 2)  # Move to end of file to get size
        file_size = file_object.tell()  # Get current position (file size)
        file_object.seek(0)  # Reset pointer back to the beginning

        if file_size > max_size:
            raise ValidationException(
                f"File size exceeds the maximum limit of {max_size} bytes. Uploaded file size: {file_size} bytes."
            )
    else:
        raise ValidationException("Invalid file object provided.")

def validate_datetime(value, format="%Y-%m-%d %H:%M:%S", before=None, before_or_equals=None, after=None, after_or_equals=None):
    date_value =  __format_date(value, format)

    if before and date_value >= __format_date(before, format):
        raise ValidationException(f"Date {value} must be before {before}.")
    if before_or_equals and date_value > __format_date(before_or_equals, format):
        raise ValidationException(f"Date {value} must be before or equals to {before_or_equals}.")
    if after and date_value <= __format_date(after, format):
        raise ValidationException(f"Date {value} must be after {after}.")
    if after_or_equals and date_value < __format_date(after_or_equals, format):
        raise ValidationException(f"Date {value} must be after or equals to {after_or_equals}.")

def __format_date(value, format="%Y-%m-%d %H:%M:%S"):
    try:
        date_value = datetime.strptime(value, format)
        return date_value
    except ValueError:
        raise ValidationException(f"Value {value} does not match the expected datetime format {format}.")
