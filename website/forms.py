import re
from django import forms
from .models import Inquiry, InquiryAntaraCares, InquiryBrandIdentity, InquiryEdubestOnline, InquiryEnhance, InquiryEvasionExotique, InquiryI2C2, InquiryIconicCity, InquiryWebsiteDesign
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class InquiryForm(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormBrandIdentity(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryBrandIdentity
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormWebsiteDesign(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryWebsiteDesign
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormEvasionExotique(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryEvasionExotique
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormEnhance(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryEnhance
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormAntaraCares(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryAntaraCares
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormIconicCity(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryIconicCity
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormI2C2(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryI2C2
        fields = ['name', 'email', 'phone', 'price']

class InquiryFormEdubestOnline(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV3)

    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = forms.CharField(
        label='Name*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Name*', 'required': True})
    )
    email = forms.EmailField(
        label='Email*',
        widget=forms.EmailInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'placeholder': 'Email*', 'required': True})
    )
    phone = forms.CharField(
        label='Phone*',
        widget=forms.TextInput(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'id': 'phone', 'placeholder': 'Phone*', 'required': True})
    )
    price = forms.ChoiceField(
        label='Choose your price*',
        choices=PRICE_CHOICES,
        widget=forms.Select(attrs={'class': 'footer-enquiry-form-input block w-full border-0 px-3.5 py-2 focus:shadow-sm placeholder:text-gray-500 focus:placeholder:text-transparent bg-transparent focus:ring-0 focus-visible:outline-0 sm:text-sm sm:leading-6 transition-all duration-500', 'required': True}),
        initial='',
        required=True
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Use regular expression to allow only digits (0-9) and the '+' symbol
        if not re.match(r'^[\d+]+$', phone):
            raise forms.ValidationError('Phone number can only contain digits and "+" symbol.')
        return phone

    class Meta:
        model = InquiryEdubestOnline
        fields = ['name', 'email', 'phone', 'price']