from django.utils.text import slugify
import uuid

def generate_slug(title:str ) -> str:

    # A function to generate unique slug for a given title

    from .models import Receipe
    title = slugify(title)

    while (Receipe.objects.filter(slug= title).exists()):
        title = f'{slugify(title)}- {str(uuid.uuid4()[:4])}'

        return title