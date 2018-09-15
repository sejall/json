import json

# a Python object (dict):
x = {
  "name": "Sejal",
  "age": 19,
  "city": "Jaipur"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
