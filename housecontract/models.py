from django.db import models
from django.conf import settings
from property.models import Property           
        
class RentContract(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="house_contract"         
    )      
    property = models.ForeignKey(                              
        Property,
        on_delete=models.CASCADE,
        related_name="house_contract"   
    )  
    tenant_name = models.CharField(max_length=100, null=True) 
    tenant_email = models.CharField(max_length=150, null=True)  
    tenant_phone = models.BigIntegerField()          
    contract_startdate = models.DateField()   

    def __str__(self):
        return f"{self.user} → {self.property} on {self.contract_startdate}"   
                          