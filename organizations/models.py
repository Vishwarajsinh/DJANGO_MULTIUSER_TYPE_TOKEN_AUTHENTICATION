from django.db import models
from gst_field.modelfields import GSTField, PANField
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# initializing size of string  

GST_STATUS = [
        ('registered_dealer', 'Registered Dealer'),
        ('unregistered_dealer', 'Unregistered Dealer'),
        ('compounding_dealer_manufecturer', 'Compounding Dealer Manufecturer'),
        ('compounding_dealer_foodbusiness', 'Compounding Dealer Foodbusiness'),
        ('compounding_dealer_others', 'Compounding Dealer others'),
    ]




# Create your models here.
class Organization(models.Model):
    GST_STATUS = [
        ('registered_dealer', 'Registered Dealer'),
        ('unregistered_dealer', 'Unregistered Dealer'),
        ('compounding_dealer_manufecturer', 'Compounding Dealer Manufecturer'),
        ('compounding_dealer_foodbusiness', 'Compounding Dealer Foodbusiness'),
        ('compounding_dealer_others', 'Compounding Dealer others'),
    ]

    FINANCIAL_YEAR = [
        ('JAN-DEC', 'JAN-DEC'),
        ('APRIL-MARCH', 'APRIL-MARCH'),
    ]

    RESIDENT_STATUS = [
        ('Resident', 'Resident'),
        ('Nonresident', 'Nonresident'),
    ]

    CONSTITUTION = [
        ('proprietoryship_individual' ,'proprietoryship_individual'),
        ('limited_liability_firm' ,'limited_liability_firm'),
        ('registed_public_limited_firm' ,'registed_public_limited_firm'),
        ('registed_private_limited_firm' ,'registed_private_limited_firm'),
        ('registred_trust' ,'registred_trust'),
        ('coerative_society','coerative_society'),
        ('a_firm' ,'a_firm'),
        ('hindu_undivided_family' ,'hindu_undivided_family'),
        ('foreign_company' ,'foreign_company'),
    ]

    INCOME_TAX_TYPE = [
        ('Individual','Individual'),
        ('hindu_undivided_family','hindu_undivided_family'),
        ('company','company'),
        ('body_of_individuals','body_of_individuals'),
        ('local_authority','local_authority'),
        ('firm','firm'),
        ('trust','trust'),
        ('association_of_persons','association_of_persons'),
        ('artificial_juridical_person','artificial_juridical_person'),
        ('government','government'),
    ]

    OCCUPATION = [
        ('Individual','Individual'),
        ('hindu_undivided_family','hindu_undivided_family'),
        ('association_of_persons','association_of_persons'),
        ('local_authority','local_authority'),
        ('arbitral_tribunal','arbitral_tribunal'),
        ('government','government'),
        ('partnership_firm','partnership_firm'),
        ('factory_under_FA_1948', 'factory__under_FA_1948'),
        ('society_under_SA_1860','society_under_SA_1860'),
        ('body_of_individuals','body_of_individuals'),
    ]

    BANK_ACC_TYPE = [
        ('current_deposits','current_deposits'),
        ('saving_deposits','saving_deposits'),
        ('recurrent_deposits','recurrent_deposits'),
        ('current_deposits','current_deposits'),
        ('fixed_deposits','fixed_deposits'),
    ]

    #owner_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    org_name = models.CharField(max_length=255, null=True, blank=False)
    mailing_name = models.CharField(max_length=255, null=True, blank=False)
    website_url = models.URLField()
    GST_status = models.CharField(max_length=255, choices = GST_STATUS)
    PAN = PANField()
    GSTIN = GSTField()
    prevyear_annual_turnover = models.IntegerField()
    finance_year = models.CharField(max_length=255, choices=FINANCIAL_YEAR)
    CIN = models.CharField(max_length=21, 
        validators=[
            RegexValidator(
            regex=r'^([L|U]{1})([0-9]{5})([A-Za-z]{2})([0-9]{4})([A-Za-z]{3})([0-9]{6})$',
            message=('CIN must be Alphanumeric'),
        ),
        ])
    resident_status = models.CharField(max_length=255, choices=RESIDENT_STATUS)
    constitution = models.CharField(max_length=255,  choices=CONSTITUTION)
    income_tax_type = models.CharField(max_length=255, choices=INCOME_TAX_TYPE)
    occupation = models.CharField(max_length=255, choices=OCCUPATION)
    is_business_entity = models.BooleanField(default=False) 
    is_body_corporate = models.BooleanField(default=False)
    company_logo = models.ImageField()
    PF_number = models.CharField(max_length=255,  validators=[
            RegexValidator(
            regex=r'^[A-Z]{2}/\d{5}/\d{7}$',
            message=('PF must be Alphanumeric'),
        ),
        ])

    address = models.TextField()
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    contact_person_name = models.CharField(max_length=255)
    office_phone = PhoneNumberField(unique=True, blank=True)
    email_address = models.EmailField()
    mobile = PhoneNumberField(unique=True, blank=True)

    bank_acc_type = models.CharField(max_length=255,  choices=BANK_ACC_TYPE)
    benificiary_bank_name = models.CharField(max_length=255)
    benificiary_name = models.CharField(max_length=255)
    acc_number = models.CharField(max_length=100)
    branch = models.CharField(max_length=255)
    IFSC = models.CharField(max_length=64)

    def __str__(self):
        return self.org_name
    
class OrganizationLocation(models.Model):
    parent_company = models.ForeignKey(Organization, on_delete=models.CASCADE,related_name='organization')
    location_code = models.CharField(max_length=64)
    location_name = models.CharField(max_length=255)
    
    GST_reg_status = models.CharField(max_length=255, choices = GST_STATUS)
    PAN = PANField()
    parent_company_GST = models.BooleanField(default=True)
    GST = GSTField()
    location_id = models.CharField(max_length=64)

    address = models.TextField()
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    contact_person_name = models.CharField(max_length=255)
    office_phone = PhoneNumberField(unique=True, blank=True)
    email_address = models.EmailField()
    mobile = PhoneNumberField(unique=True, blank=True)

    def __str__(self):
        return self.location_name
    
class LocationBranch(models.Model):
    branch_code = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)

    address = models.TextField()
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    contact_person_name = models.CharField(max_length=255)
    office_phone = PhoneNumberField(unique=True, blank=True)
    email_address = models.EmailField()
    mobile = PhoneNumberField(unique=True, blank=True)

    def __str__(self):
        return self.branch_name