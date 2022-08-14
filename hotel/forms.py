
from django import forms


class AvailabilityForm(forms.Form):

#     ROOM_CATEGORIES=(
#     ('ROYAL', 'ROYAL'),
#     ('TWIN', 'TWIN'),
#     ('EXECUTIVE', 'EXECUTIVE'),
#     ('CLASSIC', 'CLASSIC'),
#     ('SUPER', 'SUPER'),
# )
    # room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
