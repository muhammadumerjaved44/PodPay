from django import forms
from plans.models import PlansFeatures


class PlansFeaturesAdminForm(forms.ModelForm):

    CHOICES = (
        (0, 'N/A'),
        (1, 'Not Applicable'),
        (2, 'Applicable'),
    )

    pod_history = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    admin_panel = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    document_storage = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    historical_storage_documents = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    email_support = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    mobile_app = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    multiple_cards_history = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    app_notifications = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    email_notifications = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    members_history = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    dashboard = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    payments_history = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    connections = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    chat_support = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    on_call_support = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    carrier_database = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    broker_database = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    signatories_list = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)

    class Meta:
        model = PlansFeatures
        fields = "__all__"
