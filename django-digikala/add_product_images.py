import os
import django
import ssl
from urllib.request import urlretrieve
from urllib.parse import quote

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.dev"
)

django.setup()

from django.conf import settings
from stores.models import Product

image_dir = os.path.join(settings.MEDIA_ROOT, "products-avatars")
os.makedirs(image_dir, exist_ok=True)
ssl._create_default_https_context = ssl._create_unverified_context
for product in Product.objects.all():
    filename = f"product-{product.id}.png"
    filepath = os.path.join(image_dir, filename)

    url = f"https://placehold.co/600x400/png?text={quote(product.name)}"

    urlretrieve(url, filepath)

    product.image.name = f"products-avatars/{filename}"
    product.save(update_fields=["image"])

print("All product images downloaded successfully!")