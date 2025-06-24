import uuid
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from account.models import CustomUser, Role, RoleName
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = "Generate 10,000 students with role STUDENT"

    def handle(self, *args, **kwargs):
        student_role, created = Role.objects.get_or_create(name=RoleName.STUDENT)

        created_count = 0
        for _ in range(100):
            first_name = fake.first_name()
            last_name = fake.last_name()
            phone = fake.unique.phone_number()[:15]
            email = fake.unique.email()
            username = fake.unique.user_name()

            user = CustomUser(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                role=student_role,
                custom_uuid=uuid.uuid4(),
                is_worker=False,
                is_verified=True,
            )
            user.set_password("defaultpassword123")  # Или любой дефолтный пароль
            user.save()
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully created {created_count} STUDENT users"))
