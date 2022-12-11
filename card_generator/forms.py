from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from card_generator.models import CardGenerator


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
