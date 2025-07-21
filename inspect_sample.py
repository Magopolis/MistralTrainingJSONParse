import json

with open("conversations.json", "r") as f:
    data = json.load(f)

sample = data[1]  # second conversation

mapping = sample.get("mapping", {})
print(f"Top-level keys in mapping: {list(mapping.keys())[:5]}...")

for k, v in list(mapping.items())[:5]:  # show only first 5 messages
    print(f"\n🔑 Key: {k}")
    if isinstance(v, dict):
        message = v.get("message", {})
        if message:
            print("  Role:", message.get("author", {}).get("role"))
            print("  Content:", message.get("content", {}).get("parts"))
            print("  Timestamp:", message.get("create_time"))
        else:
            print("  (No message found)")
