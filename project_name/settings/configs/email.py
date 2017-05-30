import os


EMAIL_HOST = os.environ.get(
    'EMAIL_HOST', '127.0.0.1'
)
EMAIL_PORT = int(
    os.environ.get('EMAIL_HOST', 25)
)
DEFAULT_FROM_EMAIL = os.environ.get(
    'DEFAULT_FROM_EMAIL', 'User <noreply@example.ru>'
)
