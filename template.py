import os
from pathlib import Path
project_name = "ProjectX"

# Folder Structure
folders = [
    f"{project_name}/users",  # User data (if not using CMS)
    f"{project_name}/projects",  # Project data (if not using CMS)
    f"{project_name}/static",  # Static files like images, CSS, JS
    f"{project_name}/templates",  # Templates for user interface (if using a web framework)
    f"{project_name}/api",  # API endpoints for functionalities
    f"{project_name}/llm",  # LLM integration (optional)
]

# Create directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Additional files
files = [
    f"{project_name}/app.py",  # Main application script (using a web framework)
    f"{project_name}/requirements.txt",  # Project dependencies
]

# Add LLM specific files (optional)
if os.path.exists(f"{project_name}/llm"):
    files.append(f"{project_name}/llm/config.py")  # LLM configuration

for file in files:
    file_path = Path(file)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass
