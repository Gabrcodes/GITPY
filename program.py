import requests

# Replace with your GitHub username and personal access token
GITHUB_USERNAME = 'your_username'
GITHUB_TOKEN = 'your_token'

# Base URL for GitHub API
BASE_URL = 'https://api.github.com'

# Function to list repositories
def list_repos():
    url = f"{BASE_URL}/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code != 200:
        print(f"Failed to fetch repositories: {response.json().get('message')}")
        return

    repos = response.json()

    if isinstance(repos, list) and repos:
        print("\nYour Repositories:")
        for idx, repo in enumerate(repos, start=1):
            print(f"{idx}. {repo['name']} (URL: {repo['html_url']})")
    else:
        print("No repositories found.")

# Function to create a new repository
def create_repo():
    repo_name = input("Enter the name of the new repository: ")
    private = input("Should it be private? (y/n): ").lower() == 'y'

    url = f"{BASE_URL}/user/repos"
    payload = {
        "name": repo_name,
        "private": private
    }
    response = requests.post(url, json=payload, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    else:
        print(f"Failed to create repository: {response.json().get('message')}")

# Function to check branches of a specific repository
def list_branches():
    repo_name = input("Enter the name of the repository: ")
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}/branches"
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

    if response.status_code != 200:
        print(f"Failed to fetch branches: {response.json().get('message')}")
        return

    branches = response.json()

    if isinstance(branches, list) and branches:
        print(f"\nBranches in '{repo_name}':")
        for branch in branches:
            print(f"- {branch['name']}")
    else:
        print(f"No branches found for repository '{repo_name}'.")

# Main function to create a CLI
def main():
    while True:
        print("\nOptions:")
        print("1. List Repositories")
        print("2. Create a New Repository")
        print("3. List Branches in a Repository")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            list_repos()
        elif choice == '2':
            create_repo()
        elif choice == '3':
            list_branches()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
