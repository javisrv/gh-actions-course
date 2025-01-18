import subprocess

print("Installing dependencies from requirements.txt...")
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
print("Dependencies installed successfully!")