from django.db import models
from gst_field.modelfields import GSTField, PANField
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
GST_STATUS = [
    ('registered_dealer', 'Registered Dealer'),
    ('unregistered_dealer', 'Unregistered Dealer'),
    ('compounding_dealer_manufecturer', 'Compounding Dealer Manufecturer'),
    ('compounding_dealer_foodbusiness', 'Compounding Dealer Foodbusiness'),
    ('compounding_dealer_others', 'Compounding Dealer others'),
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


class UnitGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    unit_group = models.ForeignKey(UnitGroup, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Good(models.Model):

    TAX_CATEGORY = (
        ("Taxable","Taxable"),
        ("NIL rated","NIL rated"),
        ("Exampted","Exampted"),
        ("Non GST","Non GST"),
    )

    PRODUCT_CATEGORY = (
        ("finished_goods", "finished_goods"),
        ("raw_material", "raw_material"), 
        ("packing_material", "packing_material"),
        ("semi_finished_goods", "semi_finished_goods"),
        ("trading_goods", "trading_goods"),
        ("capital_goods", "capital_goods"),
    )

    name =  models.CharField(max_length = 200)
    desc = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    sub_category =  models.CharField(max_length = 200)
    unit_group =  models.CharField(max_length = 200)
    unit =  models.CharField(max_length = 200)
    tax_category =  models.CharField(max_length = 200, choices = TAX_CATEGORY)
    product_type =  models.CharField(max_length = 200, choices = PRODUCT_CATEGORY)
    MRP = models.IntegerField()
    is_tax_inclusive = models.BooleanField(default=False)
    is_free_item = models.BooleanField(default=False)
    is_stockable = models.BooleanField(default=True)
    warn_on_negative = models.BooleanField(default=True)
    is_saleable_item = models.BooleanField(default=True)
    include_stock_valuation = models.BooleanField(default=True)
    is_active_product = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField()

    hsn_code = models.IntegerField()
    hsn_decs = models.TextField()
    IGST = models.IntegerField()
    SGST = models.IntegerField()
    CGST = models.IntegerField()

    sale_unit_price = models.FloatField()
    min_sale_qty = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    purchase_unit_price = models.FloatField()
    min_sale_qty = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

class Service(models.Model):
    name = models.CharField(max_length=200)
    decs = models.TextField()
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    service_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    service_cost = models.CharField(max_length=200)

    hsn_code = models.IntegerField()
    hsn_decs = models.TextField()
    IGST = models.IntegerField()
    SGST = models.IntegerField()
    CGST = models.IntegerField()

class Supplier(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    mailing_name = models.CharField(max_length=255, null=True, blank=False)
    website_url = models.URLField()
    GST_status = models.CharField(max_length=255, choices = GST_STATUS)
    GSTIN = GSTField(null = True, blank = True)
    resident_status = models.CharField(max_length=255, choices=RESIDENT_STATUS)
    constitution = models.CharField(max_length=255,  choices=CONSTITUTION)
    income_tax_type = models.CharField(max_length=255, choices=INCOME_TAX_TYPE)
    occupation = models.CharField(max_length=255, choices=OCCUPATION)
    is_business_entity = models.BooleanField(default=False) 
    is_body_corporate = models.BooleanField(default=False)

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

class Customer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    mailing_name = models.CharField(max_length=255, null=True, blank=False)
    website_url = models.URLField()
    GST_status = models.CharField(max_length=255, choices = GST_STATUS)
    GSTIN = GSTField(null = True, blank = True)
    resident_status = models.CharField(max_length=255, choices=RESIDENT_STATUS)
    constitution = models.CharField(max_length=255,  choices=CONSTITUTION)
    income_tax_type = models.CharField(max_length=255, choices=INCOME_TAX_TYPE)
    occupation = models.CharField(max_length=255, choices=OCCUPATION)
    is_business_entity = models.BooleanField(default=False) 
    is_body_corporate = models.BooleanField(default=False)

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
