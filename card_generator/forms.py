from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from card_generator.models import CardGenerator, Usage


class CardForm(forms.ModelForm):

    class Meta:
        model = CardGenerator
        fields = ('card_status',)

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'card_status',
            ),
            ButtonHolder(Submit('submit', 'Изменить статус'))
        )


class CreateCardForm(forms.ModelForm):

    class Meta:
        model = CardGenerator
        fields = (
            'card_series',
            'number_card',
            'card_issue_date',
            'end_date_of_card_activity',
            'amount_on_the_card',
            'card_status',
        )

    def __init__(self, *args, **kwargs):
        super(CreateCardForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'card_series',
                'number_card',
                'card_issue_date',
                'end_date_of_card_activity',
                'amount_on_the_card',
                'card_status',
            ),
            ButtonHolder(Submit('submit', 'Создать карту'))
        )


class UsageForm(forms.ModelForm):

    class Meta:
        model = Usage
        fields = ('card_use_date',)

    def __init__(self, *args, **kwargs):
        super(UsageForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'card_use_date',
            ),
            ButtonHolder(Submit('submit', 'Добавить дату покупки'))
        )
