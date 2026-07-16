import os
from django.conf import settings
from django.core.files import File
from escola_online.models import Curso

for obj in Curso.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(settings.MEDIA_ROOT, obj.imagem.name)

        if os.path.exists(local_path):
            with open(local_path, "rb") as f:
                obj.imagem.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True,
                )
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado localmente para: {obj}")