import os
import subprocess

def run_git():
    root = r'C:\Users\timay\OneDrive'
    target = None
    for r, ds, fs in os.walk(root):
        if 'ofm' in ds:
            target = os.path.join(r, 'ofm')
            # Check if it has the dataset folder to be sure it's the right one
            if 'dataset' in os.listdir(target):
                break
    
    if not target:
        print("Could not find 'ofm' directory with 'dataset'.")
        return

    print(f"Working in: {target}")
    os.chdir(target)

    def run_cmd(cmd):
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
        else:
            print(result.stdout)
        return result.returncode

    # Check if remote already exists
    remotes = subprocess.run("git remote", shell=True, capture_output=True, text=True).stdout
    if "origin" in remotes:
        run_cmd("git remote remove origin")
    
    run_cmd("git remote add origin https://github.com/Go9shi/ofm.git")
    run_cmd("git add .")
    run_cmd('git commit -m "Initial commit: dataset with prompts"')
    
    # Try to push to master or main
    print("Attempting to push to master...")
    if run_cmd("git push -u origin master") != 0:
        print("Push to master failed, trying main...")
        run_cmd("git branch -M main")
        run_cmd("git push -u origin main")

if __name__ == "__main__":
    run_git()

