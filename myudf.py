# myudf.py - Jython UDFs for Pig

# Filter UDF
def pass_students(marks):
    if marks is None:
        return 'false'
    return 'true' if int(marks) > 50 else 'false'

# Eval UDF
def square(num):
    if num is None:
        return 0
    return int(num) * int(num)

