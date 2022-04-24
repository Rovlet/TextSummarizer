from django.db import models


class Text(models.Model):
    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'

    full_text = models.TextField(verbose_name='Full Text')
    source = models.CharField(max_length=255, verbose_name='Source')

    def save(self, *args, **kwargs):
        self.full_text = self.full_text.replace('\n', ' ')
        self.full_text = self.full_text.replace('\r', ' ')
        super(Text, self).save(*args, **kwargs)

class Summary(models.Model):
    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'

    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    summary = models.TextField(verbose_name='Summary')
    rating = models.IntegerField(verbose_name='Rating', default=0)
