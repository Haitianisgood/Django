from django import forms
class ContactForm(forms.Form):
    """docstring for ContactFo"""
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False,label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_mmessage(self):
        message = self.cleaned_data['message']
        num_words = len(message.splite())
        if num_words<4:
            raise forms.ValidationError("Not enough words!")
        return message

#======================================================
# class ContactForm(forms.Form):
#     """docstring for ContactFo"""
#     subject = forms.CharField()
#     email = forms.EmailField(required=False)
#     message = forms.CharField()