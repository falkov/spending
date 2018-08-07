from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals


class Receipt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    date_time = models.DateTimeField(blank=False)
    operation_type = models.IntegerField(blank=False)
    total_sum = models.IntegerField(blank=False)
    cash_total_sum = models.IntegerField(blank=False)
    e_cash_total_sum = models.IntegerField(blank=False)
    nds_18 = models.IntegerField(blank=True, default=0)
    nds_10 = models.IntegerField(blank=True, default=0)
    nds_0 = models.IntegerField(blank=True, default=0)
    nds_no = models.IntegerField(blank=True, default=0)
    store = models.CharField(blank=True, max_length=256, default="")  # поле "user" в json файле
    retail_place_address = models.CharField(blank=True, max_length=256, default="")
    store_inn = models.CharField(blank=True, max_length=13, default="")
    taxation_type = models.IntegerField(blank=True, default=0)
    kkt_reg_id = models.CharField(blank=True, max_length=21, default="")
    shift_number = models.IntegerField(blank=True, default=0)
    fiscal_document_number = models.IntegerField(blank=True, default=0)
    fiscal_drive_number = models.CharField(blank=True, max_length=17, default="")
    request_number = models.IntegerField(blank=True, default=0)
    operator = models.CharField(blank=True, max_length=65, default="")

    def __str__(self):
        return f"User = {user}, date = {self.date_time}, sum = {self.total_sum}"


class Item(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=128, default="")
    price = models.IntegerField(blank=True, default=0)
    quantity = models.FloatField(blank=True, default=0)
    nds_18 = models.IntegerField(blank=True, default=0)
    nds_10 = models.IntegerField(blank=True, default=0)
    nds_0 = models.IntegerField(blank=True, default=0)
    nds_no = models.IntegerField(blank=True, default=0)
    sum = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"Name = {self.name}, Quantity = {self.quantity}, Sum = {self.sum}"


class StornoItem(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=128, default="")
    price = models.IntegerField(blank=True, default=0)
    quantity = models.FloatField(blank=True, default=0)
    nds_18 = models.IntegerField(blank=True, default=0)
    nds_10 = models.IntegerField(blank=True, default=0)
    nds_0 = models.IntegerField(blank=True, default=0)
    nds_no = models.IntegerField(blank=True, default=0)
    sum = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"Name = {self.name}, Quantity = {self.quantity}, Sum = {self.sum}"


class ReceiptDiscountMarkup(models.Model):  # поле "modifiers " в json файле
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    discount_name = models.CharField(blank=True, max_length=128, default="")
    markup_name = models.CharField(blank=True, max_length=128, default="")
    discount = models.IntegerField(blank=True, default=0)
    markup = models.IntegerField(blank=True, default=0)
    discount_sum = models.IntegerField(blank=True, default=0)
    markup_sum = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"Discount = {self.discount_name}, Markup = {self.markup}"


class ItemDiscountMarkup(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    discount_name = models.CharField(blank=True, max_length=128, default="")
    markup_name = models.CharField(blank=True, max_length=128, default="")
    discount = models.IntegerField(blank=True, default=0)
    markup = models.IntegerField(blank=True, default=0)
    discount_sum = models.IntegerField(blank=True, default=0)
    markup_sum = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"Discount = {self.discount_name}, Markup = {self.markup}"


class StornoItemDiscountMarkup(models.Model):
    storno_item = models.ForeignKey(StornoItem, on_delete=models.CASCADE)
    discount_name = models.CharField(blank=True, max_length=128, default="")
    markup_name = models.CharField(blank=True, max_length=128, default="")
    discount = models.IntegerField(blank=True, default=0)
    markup = models.IntegerField(blank=True, default=0)
    discount_sum = models.IntegerField(blank=True, default=0)
    markup_sum = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"Discount = {self.discount_name}, Markup = {self.markup}"


class Message(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    type = models.CharField(blank=True, max_length=256, default="")
    message = models.CharField(blank=True, max_length=256, default="")

    def __str__(self):
        return f"Type = {self.type}, message = {self.message}"
