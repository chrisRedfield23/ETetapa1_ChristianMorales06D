"""
ASGI config for ETetapa1_ChristianMorales006D project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ETetapa1_ChristianMorales006D.settings')

application = get_asgi_application()
