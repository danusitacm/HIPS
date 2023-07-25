from django.db import models
class HashRecord(models.Model):
    hash_record_pk = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=200)
    hash_value = models.CharField(max_length=64)

    class Meta:
        db_table = 'hash_record'