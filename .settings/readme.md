# Settings

For security reasons, files in this folder are ignored by git

## Notification presets

File: notif.py

Example:

``` python
# Apprise format notification services <https://github.com/caronc/apprise>
services = [
    ('windows', 'windows://'), # windows notification
    ('pushbullet', 'pbul://accesstoken') # pushbullet
]
```
