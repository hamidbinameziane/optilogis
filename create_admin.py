import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') # Remplace 'core' par le nom de ton dossier settings
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='hba').exists():
    User.objects.create_superuser('hba', 'hba@example.com', '5292')
    print("Superuser créé avec succès !")
else:
    print("Le Superuser existe déjà.")