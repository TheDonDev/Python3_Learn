import subprocess
import sys

def run_git_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout

def main():
    # Get the commit message from the user
    commit_message = input("Enter commit message: ")

    # Step 1: git add .
    print("Staging all changes...")
    run_git_command("git add .")

    # Step 2: git commit -m "commit_message"
    print("Committing changes...")
    run_git_command(f'git commit -m "{commit_message}"')

    # Step 3: Determine if the branch is main or master
    print("Checking the branch...")
    branch = run_git_command("git symbolic-ref --short HEAD").strip()
    
    if branch not in ["main", "master"]:
        print(f"Detected branch: {branch}. Proceeding to push to origin/{branch}.")
    else:
        print(f"Branch is '{branch}'.")

    # Step 4: git push origin main/master
    print(f"Pushing to origin/{branch}...")
    run_git_command(f"git push origin {branch}")
    
    print("Changes pushed successfully!")

if __name__ == "__main__":
    main()
