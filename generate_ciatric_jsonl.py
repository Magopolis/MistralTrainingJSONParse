import json
from datetime import datetime, timezone
import uuid

def generate_ciatric_jsonl(input_file, output_file, subject_default='Ciatric'):
    """
    Reads a JSON file containing chat entries and writes each prompt/reply pair
    as a JSONL record with the CiatricMvp schema.
    
    Schema per record:
    {
      "id": "<unique id>",
      "timestamp": "<ISO8601 timestamp>",
      "subject": "<subject_default or from input>",
      "question": "<prompt text>",
      "answer": "<reply text>",
      "hashtags": [],  # empty list if none
      "metadata": {
        "source": "<thread title or file name>",
        "author": "<user or assistant>",
        "thread_title": "<thread title if available>"
      }
    }
    """
    with open(input_file, 'r') as f:
        data = json.load(f)

    with open(output_file, 'w') as out:
        for item in data:
            record = {
                "id": item.get("id", str(uuid.uuid4())),
                "timestamp": item.get("timestamp", datetime.now(timezone.utc).isoformat()),
                "subject": item.get("subject", subject_default),
                "question": item.get("prompt", ""),
                "answer": item.get("reply", ""),
                "hashtags": item.get("hashtags", []),
                "metadata": {
                    "source": item.get("source", input_file),
                    "author": item.get("author", "user"),
                    "thread_title": item.get("thread_title", "")
                }
            }
            out.write(json.dumps(record) + "\n")

if __name__ == "__main__":
    generate_ciatric_jsonl('conversations.json', 'ciatric_memory.jsonl')



