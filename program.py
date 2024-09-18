import requests
import json
import os

# Replace with your GitHub username and personal access token
GITHUB_USERNAME = 'your_username'
GITHUB_TOKEN = 'your_token'

# Base URL for GitHub API
BASE_URL = 'https://api.github.com'

# Function to add colored and styled outputs (fancy ZSH-like feel)
def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Fancy prompt with colors
def fancy_prompt():
    print(colored_text("\nGitHub CLI", "1;32"))
    print(colored_text("1. List Repositories", "1;36"))
    print(colored_text("2. Create a New Repository", "1;36"))
    print(colored_text("3. List Branches in a Repository", "1;36"))
    print(colored_text("4. Delete a Repository", "1;36"))
    print(colored_text("5. Update Repository Details", "1;36"))
    print(colored_text("6. List Commits in a Repository", "1;36"))
    print(colored_text("7. Exit", "1;31"))

# Function to list repositories
def list_repos():
    url = f"{BASE_URL}/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code != 200:
        print(colored_text(f"Failed to fetch repositories: {response.json().get('message')}", "1;31"))
        return

    repos = response.json()

    if isinstance(repos, list) and repos:
        print(colored_text("\nYour Repositories:", "1;32"))
        for idx, repo in enumerate(repos, start=1):
            print(f"{idx}. {repo['name']} (URL: {repo['html_url']})")
    else:
        print(colored_text("No repositories found.", "1;33"))

# Function to create a new repository
def create_repo():
    repo_name = input(colored_text("Enter the name of the new repository: ", "1;34"))
    private = input(colored_text("Should it be private? (y/n): ", "1;34")).lower() == 'y'

    url = f"{BASE_URL}/user/repos"
    payload = {
        "name": repo_name,
        "private": private
    }
    response = requests.post(url, json=payload, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code == 201:
        print(colored_text(f"Repository '{repo_name}' created successfully!", "1;32"))
    else:
        print(colored_text(f"Failed to create repository: {response.json().get('message')}", "1;31"))

# Function to delete a repository
def delete_repo():
    repo_name = input(colored_text("Enter the name of the repository to delete: ", "1;34"))

    confirm = input(colored_text(f"Are you sure you want to delete '{repo_name}'? This action cannot be undone (y/n): ", "1;31")).lower()
    if confirm != 'y':
        print(colored_text("Repository deletion aborted.", "1;33"))
        return

    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    response = requests.delete(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code == 204:
        print(colored_text(f"Repository '{repo_name}' deleted successfully!", "1;32"))
    else:
        print(colored_text(f"Failed to delete repository: {response.json().get('message')}", "1;31"))

# Function to update repository details
def update_repo():
    repo_name = input(colored_text("Enter the name of the repository to update: ", "1;34"))
    new_name = input(colored_text("Enter the new name of the repository (leave blank to keep current name): ", "1;34"))
    description = input(colored_text("Enter a new description (leave blank to keep current description): ", "1;34"))
    private = input(colored_text("Make the repository private? (y/n): ", "1;34")).lower() == 'y'

    payload = {
        "name": new_name if new_name else repo_name,
        "description": description,
        "private": private
    }
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    response = requests.patch(url, json=payload, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code == 200:
        print(colored_text(f"Repository '{repo_name}' updated successfully!", "1;32"))
    else:
        print(colored_text(f"Failed to update repository: {response.json().get('message')}", "1;31"))

# Function to list branches of a specific repository
def list_branches():
    repo_name = input(colored_text("Enter the name of the repository: ", "1;34"))
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}/branches"
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code != 200:
        print(colored_text(f"Failed to fetch branches: {response.json().get('message')}", "1;31"))
        return

    branches = response.json()

    if isinstance(branches, list) and branches:
        print(colored_text(f"\nBranches in '{repo_name}':", "1;32"))
        for branch in branches:
            print(f"- {branch['name']}")
    else:
        print(colored_text(f"No branches found for repository '{repo_name}'.", "1;33"))

# Function to list commits in a repository
def list_commits():
    repo_name = input(colored_text("Enter the name of the repository: ", "1;34"))
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}/commits"
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code != 200:
        print(colored_text(f"Failed to fetch commits: {response.json().get('message')}", "1;31"))
        return

    commits = response.json()

    if isinstance(commits, list) and commits:
        print(colored_text(f"\nCommits in '{repo_name}':", "1;32"))
        for idx, commit in enumerate(commits[:5], start=1):  # Limit to latest 5 commits
            print(f"{idx}. {commit['commit']['message']} (Author: {commit['commit']['author']['name']})")
    else:
        print(colored_text(f"No commits found for repository '{repo_name}'.", "1;33"))

# Main function to create a CLI with fancy ZSH options
def main():
    while True:
        fancy_prompt()
        choice = input(colored_text("\nChoose an option (1-7): ", "1;34"))

        if choice == '1':
            list_repos()
        elif choice == '2':
            create_repo()
        elif choice == '3':
            list_branches()
        elif choice == '4':
            delete_repo()
        elif choice == '5':
            update_repo()
        elif choice == '6':
            list_commits()
        elif choice == '7':
            print(colored_text("Exiting...", "1;31"))
            break
        else:
            print(colored_text("Invalid choice. Please try again.", "1;31"))

if __name__ == "__main__":
    main()
