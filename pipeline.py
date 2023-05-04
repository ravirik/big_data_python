import requests
import os

# Define the URL for the GitHub API
url = "https://api.github.com/repos/{owner}/{repo}/contents/{path}"

# Define the DigitalOcean server details
server_ip = "INSERT_SERVER_IP"
server_username = "INSERT_SERVER_USERNAME"
server_password = "INSERT_SERVER_PASSWORD"

# Define the repository and file path on GitHub
repo_owner = "INSERT_REPO_OWNER"
repo_name = "INSERT_REPO_NAME"
file_path = "INSERT_FILE_PATH"

# Make a GET request to the GitHub API to retrieve the file contents.
response = requests.get(url.format(owner=repo_owner, repo=repo_name, path=file_path))

# Extract the content from the response JSON
content = response.json()["content"]

# Decode the Base64-encoded content
decoded_content = base64.b64decode(content).decode("utf-8")

# Write the decoded content to a file on the DigitalOcean server
with open("data.txt", "w") as f:
    f.write(decoded_content)

# Use SCP to transfer the file to the DigitalOcean server
os.system(f"scp data.txt {server_username}@{server_ip}:~/data.txt")

# Remove the temporary file
os.remove("data.txt")
