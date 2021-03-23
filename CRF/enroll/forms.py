from django import forms

truefalse = (
	('Yes', 'Yes'),
	('No', 'No')
	)

class PatientForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	age = forms.IntegerField(min_value = 0)

class InclusionForm(forms.Form):
	ans_text = forms.ChoiceField(choices=truefalse)