# 7learn.com crawler
This script crawls all courses in 7learn academy and extracts:
1. Course name
2. Course teacher
3. Course description
4. Course longtime
5. Course price
6. Course cover-image

## How to use
### First intall requirements
```
pip install -r requirements.txt
```

### Now you can use one of the following commands 
To find all courses links:
```
python main.py extract_courses
```
To exctact data from founded courses:
```
python main.py extract_pages
```

## Saving mode:
You can save extacted data in some .json files or in Mongodb.

### To save in.json documents go to cinfig.py:

```python
SAVE_MODE = "json-document"
```
### To save Mongodb documents go to cinfig.py:
> Run Mongodb on (localhost, 27017) or change mongodb.py file.
```python
SAVE_MODE = "mongodb"
```
>