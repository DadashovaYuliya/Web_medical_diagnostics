from django.urls import reverse
from rest_framework.test import APITestCase

from medic.models import Service


class ServiceTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.service = Service.objects.create(
            name="Анализ", description="Анализ крови", price=100)

    def test_about_page(self):
        url = reverse('medic:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contacts_post(self):
        url = reverse('medic:contacts')
        data = {'name': 'Юлия', 'phone': '123456789'}
        response = self.client.post(url, data)
        response_text = response.content.decode('utf-8')
        self.assertIn('Спасибо, Юлия! Ваше сообщение получено.', response_text)
        self.assertIn('Ответ будет направлен по номеру: 123456789.', response_text)

    def test_service_detail(self):
        """Тестирование получения услуги."""
        url = reverse("medic:services_detail", args=(self.service.pk,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services_detail.html')
        self.assertEqual(response.context['service'], self.service)
