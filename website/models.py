from django.db import models

# Create your models here.

class Inquiry(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Home Page - Inquiry"
        verbose_name_plural = "Home Page - Inquiries"

class InquiryBrandIdentity(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Brand Identity - Inquiry"
        verbose_name_plural = "Brand Identity - Inquiries"

class InquiryWebsiteDesign(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Website Design - Inquiry"
        verbose_name_plural = "Website Design - Inquiries"

class InquiryEvasionExotique(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Evasion Exotique - Inquiry"
        verbose_name_plural = "Evasion Exotique - Inquiries"

class InquiryEnhance(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Enhance - Inquiry"
        verbose_name_plural = "Enhance - Inquiries"

class InquiryAntaraCares(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Antara Cares - Inquiry"
        verbose_name_plural = "Antara Cares - Inquiries"

class InquiryIconicCity(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Iconic City - Inquiry"
        verbose_name_plural = "Iconic City - Inquiries"

class InquiryI2C2(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "I2C2 - Inquiry"
        verbose_name_plural = "I2C2 - Inquiries"

class InquiryEdubestOnline(models.Model):
    PRICE_CHOICES = [
        ('', 'Choose your price*'),
        ('1000 - 3000 USD', '1000 - 3000 USD'),
        ('3000 - 6000 USD', '3000 - 6000 USD'),
        ('6000 - 10,000 USD', '6000 - 10,000 USD'),
        ('Over 10,000 USD', 'Over 10,000 USD'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Edubest Online - Inquiry"
        verbose_name_plural = "Edubest Online - Inquiries"