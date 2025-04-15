# SonarQube Main Branch Rename CLI

A simple Python CLI script to rename the **main branch** of a SonarQube project using the `api/project_branches/rename` endpoint (SonarQube 2025.1+ compatible).

---

## Requirements

- Python 3.6+
- `requests` library (`pip install requests`)
- A valid [SonarQube token](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/managing-tokens/)

---

## Environment Variable

Before using the script, export your SonarQube authentication token:

```bash
export SONAR_TOKEN=your_sonar_token
```

---

## Usage

```bash
./sq_mbr.py \
  --url https://sonarqube.example.com \
  --project my_project_key \
  --name new_main_branch_name
```

### Arguments

| Argument      | Description                           |
|---------------|---------------------------------------|
| `--url`       | SonarQube base URL                    |
| `--project`   | Project key in SonarQube              |
| `--name`      | New name for the main branch          |

---

## Example

```bash
export SONAR_TOKEN=sqp_abcd1234efgh5678ijkl9012

chmod +x ./sq_mbr.py

./sq_mbr.py \
  --url https://sonarqube.mycompany.com \
  --project my-service \
  --name main-renamed
```

If successful, you will see:

```
Main branch for project 'my-service' successfully renamed to 'main-renamed'.
```

---

## Notes

- This script is designed for SonarQube **2025.1 and later**, where only `project` and `name` parameters are required.
- The script renames the **main branch** only. It does not rename arbitrary feature branches.
