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

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, price):
        product = Product(name=name, price=price)
        product.save()
        return CreateProduct(product=product)

class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        price = graphene.Float()

    product = graphene.Field(ProductType)

    def mutate(self, info, id, name=None, price=None):
        product = Product.objects.get(id=id)
        if name:
            product.name = name
        if price:
            product.price = price
        product.save()
        return UpdateProduct(product=product)

class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        product = Product.objects.get(id=id)
        product.delete()
        return DeleteProduct(success=True)

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()