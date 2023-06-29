from django import forms
from .models import Reply


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']

    def update_reply_text(self, new_text):
        self.instance.reply_text = new_text
        self.instance.save()

    def delete_reply(self):
        self.instance.delete()
