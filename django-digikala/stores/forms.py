# form are only for page sites not admin panel 
from django import forms 
from .models import *

# forms are class based in django and should be inherited from forms.ModelForm
# register
class StoreForm(forms.ModelForm):
    class Meta():
        # it sets that forms works with Store model
        # فرم قرار است یک نمونه از مدل Store بسازد
        model= Store
        # مشخص می‌کند  چه فیلدهایی در فرم نمایش داده شود
        fields= ['name','description']
        # django uses Textarea by default for textfield attr we just wan to set lines to 4
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ProductForm(forms.ModelForm):
    class Meta():
        # it sets that forms works with Product model
        model= Product
        # مشخص می‌کند  چه فیلدهایی در فرم نمایش داده شود
        fields= ['name','price','description','image','stock']
        # django uses Textarea by default for textfield attr we just wan to set lines to 4
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
