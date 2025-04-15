#!/usr/bin/env python3

import argparse
import os
import requests
import sys


def rename_main_branch(sonarqube_url, project_key, new_branch_name, token):
    api_endpoint = f"{sonarqube_url}/api/project_branches/rename"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"project": project_key, "name": new_branch_name}

    response = requests.post(api_endpoint, headers=headers, data=payload)

    if response.status_code == 204:
        print(
            f"Main branch for project '{project_key}' successfully renamed to '{new_branch_name}'."
        )
    else:
        print(f"Failed to rename main branch: {response.status_code} {response.reason}")
        try:
            print("Response:", response.json())
        except Exception:
            print("Raw response:", response.text)


def main():
    parser = argparse.ArgumentParser(
        description="Rename the main branch of a SonarQube project (2025.1+)."
    )
    parser.add_argument(
        "--url",
        required=True,
        help="SonarQube base URL (e.g., https://sonarqube.example.com)",
    )
    parser.add_argument("--project", required=True, help="SonarQube project key")
    parser.add_argument("--name", required=True, help="New name for the main branch")

    args = parser.parse_args()

    token = os.getenv("SONAR_TOKEN")
    if not token:
        print("Environment variable SONAR_TOKEN is not set.")
        sys.exit(1)

    rename_main_branch(args.url, args.project, args.name, token)


if __name__ == "__main__":
    main()
