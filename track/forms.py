from django import forms


class GenreForm(forms.Form):
    CHOICES = (('rock', 'Rock'), ('alternative rock', 'Alternative Rock'), ('pop', 'Pop'), ('country', 'Country'),
               ('electronic', 'Electronic'), ('jazz', 'Jazz'), ('r&b', 'R&B'), ('rap', 'Rap'), ('reggae', 'Reggae'))
    genres = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class' : 'custom-select'}))
