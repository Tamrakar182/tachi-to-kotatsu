# Tachiyomi to Kotatsu

Making this to convert tachiyomi backup files to kotatsu backup files so that I can migrate to kotatsu.

## Tachiyomi Extraction
The data types present in tachiyomi is in ```tachi_classes.proto```. Compiling this proto file will give us the python classes to read the tachiyomi backup files. From the tachiyomi backup files, we can get the majorly following data:
- Backup Categories
- Backup Sources
- Backup Manga (huge data type with all the tracking, chapter info, etc.)

Backup Manga has most of the data that we need.

## Kotatsu Conversion

Kotatsu zips 6 json files into a single zip. It includes the following data:

### Bookmarks

### Categories
```json
{
    "category_id": 1,
    "created_at": 1704781699296,
    "sort_key": "<Order from tachi file(first one doesnt have a number)>",
    "title": "<Category Name>",
    "order": "NEWEST",
    "track": true,
    "show_in_lib": true
}
```
The default will be used for the fields not present in the tachiyomi backup file. We only get the order/sort_key and title from the tachiyomi backup file. The rest will be set to default.

### Favorites

### History

### Index (default used)
```json
  {
    "app_id": "org.koitharu.kotatsu",
    "app_version": 610,
    "created_at": 1704781796582
  }
```
Contains the app version and app id. Not sure if this is needed. Default will be used

### Settings (default used)
Contains all the settings details. My default settings will be used.

### Sources
```json
{
    "source": "<source name>",
    "enabled": false,
    "sort_key": 832
}
```
The sources files has the list of all the sources available to kotatsu. Matching against the ones in tachiyomi, we can set the sources for the library to enables and sort so that the active sources are at top.


## Checklist
- [x] Unzip tachiyomi backup files
- [x] Read tachiyomi backup files
- [x] Convert tachiyomi backup files to json
- [ ] Convert json to seperate kotatsu backup files
- [ ] Conversion to Kotatsu Sources File
- [ ] Conversion to Kotatsu Categories File
- [ ] Conversion to Kotatsu Library File

## Enviroment Setup

### Create Virtual Environment
```python -m venv .\venv```

### Activate Virtual Environment
```venv\Scripts\activate.bat```

### Install all the Dependencies
```pip install -r requirements.txt```