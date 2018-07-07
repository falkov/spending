from django.db import models

# Create your models here.

class Section(models.Model):
    section_number = models.IntegerField(default=0)
    text_eng = models.CharField(max_length=80, default="")
    text_rus = models.CharField(max_length=80, default="")
    text_nor = models.CharField(max_length=80, default="")

    def __str__(self):
        return self.text_eng


class Question(models.Model):
    number = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text_eng = models.CharField(max_length=300, default="")
    text_rus = models.CharField(max_length=300, default="")
    text_nor = models.CharField(max_length=300, default="")
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.text_eng


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    letter = models.CharField(max_length=1, default="")
    text_eng = models.CharField(max_length=300, default="")
    text_rus = models.CharField(max_length=300, default="")
    text_nor = models.CharField(max_length=300, default="")
    correct = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.text_eng

"""
operationType 
operatorAddress 
buyerAddress 
retailPlaceAddress 
taxationType 
bankAgentRemuneration 
paymentAgentRemuneration 
dateTime 
operatorInn 
userInn 
totalSum 
operator 
operatorName 
cashTotalSum 
items 
stornoItems 
kktRegId 
shiftNumber 
fiscalDocumentNumber 
fiscalDriveNumber 
requestNumber 
bankAgentOperation 
bankSubagentOperation 
user 
bankAgentPhone 
paymentAgentPhone 
operatorPhoneToTransfer 
fiscalSign 
ecashTotalSum 
modifiers 
bankSubagentPhone 
paymentSubagentPhone 
properties 
nds18 
nds10 
nds0 
ndsNo 
ndsCalculated18 
ndsCalculated10 
addressToCheckFiscalSign 
message
senderAddress 
operatorPhoneToReceive 
rawData 
"""