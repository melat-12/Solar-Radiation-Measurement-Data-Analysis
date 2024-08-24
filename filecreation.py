import os

# Define the folder structure
folder_structure = {
    ".vscode": {
        "settings.json": "{}"
    },
    ".github": {
        "workflows": {
            "unittests.yml": "# Sample workflow"
        }
    },
    ".gitignore": "# Sample .gitignore",
    "requirements.txt": "# Sample requirements",
    "README.md": "# Solar Radiation Measurement Data Analysis",
    "src": {},
    "notebooks": {
        "__init__.py": "",
        "README.md": "# Notebooks"
    },
    "tests": {
        "__init__.py": ""
    },
    "scripts": {
        "__init__.py": "",
        "README.md": "# Scripts"
    }
}

def create_folder_structure(structure, base_path):
    for item, value in structure.items():
        current_path = os.path.join(base_path, item)
        if isinstance(value, dict):
            os.makedirs(current_path, exist_ok=True)
            create_folder_structure(value, current_path)
        else:
            os.makedirs(os.path.dirname(current_path), exist_ok=True)
            with open(current_path, "w") as f:
                f.write(value)

# Set the base path
base_path = r"C:\Users\Melat\Solar-Radiation-Measurement-Data-Analysis"

# Create the folder structure
create_folder_structure(folder_structure, base_path)