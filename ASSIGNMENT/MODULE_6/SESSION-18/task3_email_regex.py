import re

text = """
Great food! Contact support at support@gmail.com.
My email is mahek@yahoo.com.
Restaurant manager can be contacted at manager@zomato.com.
Some random text here.
"""

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

emails = re.findall(pattern, text)

print("Email Addresses:", emails)