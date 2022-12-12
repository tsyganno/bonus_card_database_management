from django.contrib import admin

from card_generator.models import CardGenerator, Usage


class CardGeneratorAdmin(admin.ModelAdmin):
    list_display = (
        'card_series',
        'number_card',
        'card_issue_date',
        'end_date_of_card_activity',
        'amount_on_the_card',
        'card_status'
    )
    list_display_links = (
        'card_series',
        'number_card',
    )
    search_fields = (
        'card_series',
        'number_card',
        'card_issue_date',
        'end_date_of_card_activity',
        'card_activation_date',
    )


class UsageAdmin(admin.ModelAdmin):
    list_display = ('card_use_date',)
    list_display_links = ('card_use_date',)
    search_fields = ('card_use_date',)


admin.site.register(CardGenerator, CardGeneratorAdmin)
admin.site.register(Usage, UsageAdmin)
