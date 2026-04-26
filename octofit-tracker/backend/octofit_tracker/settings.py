INSTALLED_APPS = [
    "djongo",
]

ALLOWED_HOSTS = [
    "localhost",
    "${CODESPACE_NAME}-8000.app.github.dev",
]

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "octofit_db",
    }
}
