from django.contrib import admin
from django.utils.timezone import make_aware
from datetime import datetime

class BaseDateSearchModelAdmin(admin.ModelAdmin):
    def get_search_results(self, request, queryset, search_term):
        if search_term:
            try:
                data_inicial, data_final = search_term.split('-')
                data_inicial = datetime.strptime(data_inicial.strip(), '%d/%m/%Y %H:%M')
                data_final = datetime.strptime(data_final.strip(), '%d/%m/%Y %H:%M')
                # data_inicial = make_aware(datetime.combine(data_inicial, datetime.min.time()))
                # data_final = make_aware(datetime.combine(data_final, datetime.max.time()))
                queryset = queryset.filter(created_at__range=(data_inicial, data_final))
                return queryset, False
            except ValueError:
                pass
        return super().get_search_results(request, queryset, search_term)