import re

text = """
Hello, contact me at 9876543210.
The phone number 8123456789 is also available.
Price is 999 and order number is 123456.
You can also WhatsApp 7123456789.
"""

pattern = r"\b[789]\d{9}\b"

phone_numbers = re.findall(pattern, text)

print("Phone Numbers:", phone_numbers)