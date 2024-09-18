# GitHub CLI Tool

This is a command-line interface (CLI) tool to interact with your GitHub repositories. The tool allows you to manage your repositories, create new ones, update or delete existing ones, and view commits and branches. The interface is styled for a ZSH-like feel with color-coded options and interactive prompts.

## Features

- **List Repositories**: Displays all repositories associated with your GitHub account.
- **Create a New Repository**: Create a new repository with the option to make it public or private.
- **List Branches**: View all branches in a specified repository.
- **Delete a Repository**: Permanently delete a repository after confirmation.
- **Update Repository**: Modify the name, description, or privacy settings of an existing repository.
- **List Commits**: View the latest 5 commits from a specified repository.
- **ZSH-Like Styling**: Fancy colored and styled CLI options for a polished experience.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/github-cli-tool.git
    ```

2. Install the required libraries:
    ```bash
    pip install requests
    ```

3. Set up your GitHub username and personal access token inside the script:
    ```python
    GITHUB_USERNAME = 'your_username'
    GITHUB_TOKEN = 'your_personal_access_token'
    ```

   > **Note:** You can generate a GitHub personal access token from your GitHub account [here](https://github.com/settings/tokens).

## Usage

To run the CLI, simply execute the script:
```bash
python github_cli.py
