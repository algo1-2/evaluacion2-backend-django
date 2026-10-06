from django.test import TestCase, Client
from django.urls import reverse


class MovieAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_vista_inicio_status_y_template(self):
        """Verifica que la página de inicio cargue correctamente con código 200 y herede de base.html"""
        url = reverse('home:inicio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inicio.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Ciencia Ficción')
        self.assertContains(response, 'Animación')
        self.assertContains(response, 'Benjamín Rivas')

    def test_vista_genero_ciencia_ficcion(self):
        """Verifica que el género ciencia-ficción muestre al menos dos películas con sus datos"""
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
        """Verifica que el género animación muestre sus películas, imágenes y clasificación"""
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
        """Verifica que una categoría no registrada devuelva HTTP 404 adecuadamente"""
        url = reverse('home:genero', kwargs={'slug_genero': 'categoria-inexistente'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
