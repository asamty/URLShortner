from django.db import models
import string, random

class Shortener(models.Model):
    short_code = models.CharField(max_length=6, unique=True, blank=True, null=True)
    original_url = models.URLField()
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Shortened url"
        verbose_name_plural = "Shortened urls"

    def __str__(self) -> str:
        return self.short_code

    def save(self, *args, **kwargs):
        """
        Function to save record with generated short code
        """
        length = 6 #length of code (token as in terms of reference)
        char = string.ascii_uppercase + string.digits + string.ascii_lowercase #any letters and digits for url code
        code = ''.join(random.choice(char) for x in range(length)) #url code with lenght of 6 with any letters and digits
        if not self.short_code:
            self.short_code = code

        super().save(*args, **kwargs)