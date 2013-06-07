from django.conf import settings


settings.configure(
    SESSION_ENGINE='redis_sessions.session',
    SESSION_REDIS_PREFIX='django_sessions',
    INSTALLED_APPS=('django.contrib.sessions', 'redis_sessions')
)
