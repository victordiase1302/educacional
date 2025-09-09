from django.db import models


class Training(models.Model):
    prompt = models.TextField(verbose_name='Pergunta')
    completion = models.TextField(verbose_name='Resposta')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Treinamento ativo'
    )
    def __str__(self):
        return self.prompt

    class Meta:
        ordering = ("-updated_at",)
        verbose_name = 'Treinamento | Cadastro'
        verbose_name_plural = 'Treinamentos | Cadastros'
