from django import forms


# Для строки поиска
class SearchForm(forms.Form):
    search = forms.CharField(max_length=120)