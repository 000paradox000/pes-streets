from django.db import models


class BaseModelQuerySet(models.QuerySet):
    pass


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db)


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   db_index=True)

    updated = models.DateTimeField(auto_now=True,
                                   editable=False,
                                   db_index=True)
    objects = BaseModelManager()

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        abstract = True
