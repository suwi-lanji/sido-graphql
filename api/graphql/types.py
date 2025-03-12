from graphene_django import DjangoObjectType
from apps.credits.models import Credit
from apps.expenses.models import Expense
from apps.inventory.models import InventoryAdjustment
from apps.products.models import Product
from apps.purchase.models import Purchase
from apps.sales.models import Sale

class CreditType(DjangoObjectType):
    class Meta:
        model = Credit
        fields = "__all__"

class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense
        fields = "__all__"

class InventoryAdjustmentType(DjangoObjectType):
    class Meta:
        model = InventoryAdjustment
        fields = "__all__"

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"

class PurchaseType(DjangoObjectType):
    class Meta:
        model = Purchase
        fields = "__all__"

class SaleType(DjangoObjectType):
    class Meta:
        model = Sale
        fields = "__all__"