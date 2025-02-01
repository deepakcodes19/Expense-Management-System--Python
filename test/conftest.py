import os
import sys

# Get the directory of the current file
current_dir = os.path.dirname(__file__)

# Join the current directory with the parent directory to get the project root
project_root = os.path.join(current_dir, '..')

# Print the project root
print("PROJECT ROOT:", project_root)

# Add the project root to the system path
sys.path.insert(0, project_root)

# Print the updated system path
print(sys.path)

