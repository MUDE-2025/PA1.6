import os

# Run me in VS Code!
# Click the triangle button in the top right, "Run Python file"
print('\n')
print('If you see this message in your CLI, VS Code is set up properly!')
print('\n  Note the command executed above in the CLI. The button uses')
print('  the Python interpreter to run the script (this file)')
print('\n')
print(f"Current Conda environment: {os.environ.get('CONDA_DEFAULT_ENV', 'Not in a Conda environment')}")