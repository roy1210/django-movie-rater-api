- djangorest-framework
- django-cors-header: To fix CORS problem when serve with react

## To allow front-end url domain to do cross-site requests

Add URL in `CORS_ORIGIN_WHITELIST` in settings.py

example: <br>
movierater/settings.py<br>
```
CORS_ORIGIN_WHITELIST = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]
```