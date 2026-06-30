# API

## Background Context

Old-school system administrators usually only know Bash. The new generation of SREs know more than just Bash scripting. This project uses a REST API to access employee data and export it to different data structures using Python.

## Requirements

- Python 3 (version 3.4.3)
- Libraries: `requests` (install with `pip3 install requests`)
- PEP 8 style
- All files must be executable

## Tasks

### 0. Gather data from an API
```bash
python3 0-gather_data_from_an_API.py <employee_id>
```

### 1. Export to CSV
```bash
python3 1-export_to_CSV.py <employee_id>
# Creates <employee_id>.csv
```

### 2. Export to JSON
```bash
python3 2-export_to_JSON.py <employee_id>
# Creates <employee_id>.json
```

### 3. Dictionary of list of dictionaries
```bash
python3 3-dictionary_of_list_of_dictionaries.py
# Creates todo_all_employees.json
```
