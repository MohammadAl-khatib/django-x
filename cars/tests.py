from django.test import TestCase
from django.urls import reverse

class CarTest(TestCase):

    def test_car_list_view_status(self):
        response = self.client.get(reverse("car_list"))
        self.assertEqual(response.status_code, 200)
    
    def test_car_list_view_template(self):
        response = self.client.get(reverse("car_list"))
        self.assertTemplateUsed(response, "cars/car_list.html")

    def test_car_create_view(self):
        response = self.client.post(
            reverse("car_create"),
            {
                "name": "car",
                "price": "2",
                "image": 'not defined',
            }, follow=True
        )

        self.assertRedirects(response, reverse("car_list"))
        self.assertContains(response, "car")