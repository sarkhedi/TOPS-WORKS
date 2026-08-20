insta_filter = ("Clarendon","Juno","Valencia","Lark")

# Trying to update the second filter
# This will give an error because tuples are immutable
insta_filter[1] = "Vintage"

print(insta_filter)

