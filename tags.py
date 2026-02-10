# "Given a list of user dictionaries, each containing a list of tags:

# Print the second tag of the first user

# Print all tags for all users (loop)"	"Example structure

# users = [
#   {""name"": ""Alice"", ""tags"": [""admin"", ""backend""]},
#   {""name"": ""Bob"", ""tags"": [""frontend""]}
# ]"


users = [
  {"name": "Alice", "tags": ["admin", "backend"]},
  {"name": "Bob", "tags": ["frontend"]}
]
print(users[0]["tags"][1])
for user in users:
    for tag in user["tags"]:
        print(tag)