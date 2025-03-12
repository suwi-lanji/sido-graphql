import graphene
from .types import (
    CreditType,
    ExpenseType,
    InventoryAdjustmentType,
    ProductType,
    PurchaseType,
    SaleType,
)
from apps.credits.models import Credit
from apps.expenses.models import Expense
from apps.inventory.models import InventoryAdjustment
from apps.products.models import Product
from apps.purchase.models import Purchase
from apps.sales.models import Sale

class Query(graphene.ObjectType):
    all_credits = graphene.List(CreditType)
    all_expenses = graphene.List(ExpenseType)
    all_inventory_adjustments = graphene.List(InventoryAdjustmentType)
    all_products = graphene.List(ProductType)
    all_purchases = graphene.List(PurchaseType)
    all_sales = graphene.List(SaleType)
    credits_by_amount = graphene.List(
        CreditType,
        min_amount=graphene.Float(),
        max_amount=graphene.Float(),
    )
    products_by_price_range = graphene.List(
        ProductType,
        min_price=graphene.Float(),
        max_price=graphene.Float(),
    )
    def resolve_all_credits(self, info, **kwargs):
        return Credit.objects.all()

    def resolve_all_expenses(self, info, **kwargs):
        return Expense.objects.all()

    def resolve_all_inventory_adjustments(self, info, **kwargs):
        return InventoryAdjustment.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_all_purchases(self, info, **kwargs):
        return Purchase.objects.all()

    def resolve_all_sales(self, info, **kwargs):
        return Sale.objects.all()
    def resolve_credits_by_amount(self, info, min_amount=None, max_amount=None, **kwargs):
        credits = Credit.objects.all()
        if min_amount:
            credits = credits.filter(amount__gte=min_amount)
        if max_amount:
            credits = credits.filter(amount__lte=max_amount)
        return credits

    def resolve_products_by_price_range(self, info, min_price=None, max_price=None, **kwargs):
        products = Product.objects.all()
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)
        return products