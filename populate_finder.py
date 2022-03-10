import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pandafidner.settings')

import django
django.setup()

from finder.models import Category, Restaurant