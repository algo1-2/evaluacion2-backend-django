from django.test import TestCase, Client
from django.urls import reverse


class MovieAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_vista_inicio_status_y_template(self):
        url = reverse('home:inicio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inicio.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Ciencia Ficción')
        self.assertContains(response, 'Animación')
        self.assertContains(response, 'Benjamín Rivas')

    def test_vista_genero_ciencia_ficcion(self):
        url = reverse('home:genero', kwargs={'slug_genero': 'ciencia-ficcion'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genero.html')
        self.assertContains(response, 'Interstellar')
        self.assertContains(response, 'The Matrix')
        self.assertContains(response, 'Blade Runner 2049')
        self.assertContains(response, '+13 años')
        self.assertContains(response, 'images/interstellar.svg')

    def test_vista_genero_animacion(self):
        url = reverse('home:genero', kwargs={'slug_genero': 'animacion'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genero.html')
        self.assertContains(response, 'Spider-Man: Into the Spider-Verse')
        self.assertContains(response, 'Coco')
        self.assertContains(response, 'El Viaje de Chihiro')
        self.assertContains(response, 'Todo Espectador')
        self.assertContains(response, 'images/coco.svg')

    def test_genero_inexistente_retorna_404(self):
        url = reverse('home:genero', kwargs={'slug_genero': 'categoria-inexistente'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
