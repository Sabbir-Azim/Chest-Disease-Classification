import os

# Ensure the artifacts directory exists
os.makedirs("artifacts", exist_ok=True)

# The message to save
text = "Hello, My name is Sabbir Azim. I am a software engineer and I am working on a project related to MLOps. Below are the recent edits made to the files in the project:\n"

# Save the message to artifacts/text.txt
with open("artifacts/text.txt", "w") as f:
    f.write(text)

print("✅ stage_01.py: artifacts/text.txt has been written.")

