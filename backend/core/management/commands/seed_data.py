from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import MenuItem, TableOrder, DiningTable
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusRestaurant with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusrestaurant.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if MenuItem.objects.count() == 0:
            for i in range(10):
                MenuItem.objects.create(
                    name=f"Sample MenuItem {i+1}",
                    category=random.choice(["starters", "main_course", "desserts", "beverages", "specials"]),
                    price=round(random.uniform(1000, 50000), 2),
                    cost=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["available", "unavailable", "seasonal"]),
                    veg=random.choice([True, False]),
                    spice_level=random.choice(["mild", "medium", "hot"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 MenuItem records created'))

        if TableOrder.objects.count() == 0:
            for i in range(10):
                TableOrder.objects.create(
                    table_number=f"Sample {i+1}",
                    server=f"Sample {i+1}",
                    items_count=random.randint(1, 100),
                    subtotal=round(random.uniform(1000, 50000), 2),
                    tax=round(random.uniform(1000, 50000), 2),
                    total=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["open", "preparing", "served", "billed", "closed"]),
                    order_time=date.today() - timedelta(days=random.randint(0, 90)),
                    payment=random.choice(["cash", "card", "upi"]),
                )
            self.stdout.write(self.style.SUCCESS('10 TableOrder records created'))

        if DiningTable.objects.count() == 0:
            for i in range(10):
                DiningTable.objects.create(
                    table_number=f"Sample {i+1}",
                    capacity=random.randint(1, 100),
                    section=random.choice(["indoor", "outdoor", "private", "bar"]),
                    status=random.choice(["available", "occupied", "reserved"]),
                    reserved_name=f"Sample DiningTable {i+1}",
                    reserved_time=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 DiningTable records created'))
