import re

text = "My phone number is 9876543210 and my alternate number is 8123456789."

masked_text = re.sub(r"\b[789]\d{5}(\d{4})\b", r"******\1", text)

print(masked_text)