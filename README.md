# Extractinator

A tool that processes a source folder to extract zip files, including nested zips, and organizes all files and folders into a specified output directory.

### Usage

```
docker compose -p extractinator exec extractinator bash
```

#### Run

```
python main.py
```

#### Reset output folder

```
rm -rf output/ && mkdir output
```
