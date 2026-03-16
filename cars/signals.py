from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver 
from cars.models import Car, CarInventory


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_valor = Car.objects.aggregate(
        total_value = Sum('valor')
    )['total_value'] or 0
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_valor=cars_valor
    )


@receiver(post_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio= 'Bio gerada automaticamente!'



@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    if created:
        car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

    