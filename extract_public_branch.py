from datetime import datetime
import os
import shutil
import sys
from git import Repo, GitCommandError


def switch_branch_and_extract(repo_path, target_branch, folder_to_extract, folder_doc, destination_branch="master", remote_name='origin'):
    try:
        # Open the repository
        repo = Repo(repo_path)

        if repo.is_dirty():
            print("Error: Repository has uncommitted changes. Please commit or stash them first.")
            return
        
        # Check if target branch exists
        if target_branch not in repo.branches:
            print(f"Error: Branch '{target_branch}' does not exist.")
            return
        
        # Switch to the target branch
        print(f"Switching to branch '{target_branch}'...")
        repo.git.checkout(target_branch)
        
        # Ensure the folder exists in the target branch
        folder_path = os.path.join(repo_path, folder_to_extract)
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_to_extract}' does not exist in branch '{target_branch}'.")
            return
        
        temp_path = os.path.dirname(repo_path)
        # Create a temporary location to store the folder contents
        temp_folder = os.path.join(temp_path, "temp_folder")
        if os.path.exists(temp_folder):
            shutil.rmtree(temp_folder)
        shutil.copytree(folder_path, temp_folder)
        print(f"Copied '{folder_to_extract}' to a temporary folder {temp_folder}.")
        
        # Switch to the destination branch
        print(f"Switching to branch '{destination_branch}'...")
        repo.git.checkout(destination_branch)
        
        # Copy the folder from the temporary location to the destination branch
        destination_folder = os.path.join(repo_path, folder_doc)
        if os.path.exists(destination_folder):
            shutil.rmtree(destination_folder)
        shutil.copytree(temp_folder, destination_folder)
        
        # Stage and commit the changes
        current_datetime = datetime.now()
        repo.git.add(folder_doc)
        repo.index.commit(f"Extracted '{folder_to_extract}' from branch '{target_branch}' to '{destination_branch}' at {current_datetime}.")
        print(f"Committed changes to branch '{destination_branch}'.")
        
        # Clean up temporary folder
        shutil.rmtree(temp_folder)
        print("Temporary folder removed.")

        remote = repo.remote(name=remote_name)
        print(f"Pushing branch '{destination_branch}' to remote '{remote_name}'...")
        remote.push(refspec=f"{destination_branch}:{destination_branch}")

        print("Push completed successfully.")

    except GitCommandError as e:
        print(f"Git command error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <target_branch>")
    else:
        file_path = os.path.abspath(__file__)
        parent_directory = os.path.dirname(file_path)
        repo_path = parent_directory
        target_branch = sys.argv[1]
        folder_to_extract = 'public'
        folder_doc = 'docs'
        switch_branch_and_extract(repo_path, target_branch, folder_to_extract, folder_doc)
