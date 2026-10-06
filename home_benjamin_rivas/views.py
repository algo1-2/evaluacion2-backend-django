from django.shortcuts import render
from django.http import Http404

# Catálogo de géneros y películas
CATALOGO_GENEROS = {
    'ciencia-ficcion': {
        'slug': 'ciencia-ficcion',
        'nombre': 'Ciencia Ficción',
        'icono': 'bi-rocket-takeoff-fill',
        'color': 'info',
        'banner': 'Explora futuros distópicos, viajes intergalácticos y tecnología de frontera.',
        'descripcion': 'Historias futuristas, viajes interestelares, realidades virtuales y tecnología avanzada que desafían los límites de la mente humana y el universo.',
        'peliculas': [
            {
                'id': 1,
                'nombre': 'Interstellar',
                'director': 'Christopher Nolan',
                'año': 2014,
                'edad': '+13 años',
                'edad_minima': 13,
                'imagen': 'images/interstellar.svg',
                'sinopsis': 'Un grupo de científicos y exploradores viaja a través de un agujero de gusano en el espacio en un intento desesperado por asegurar la supervivencia de la humanidad.',
                'destacada': True,
            },
            {
                'id': 2,
                'nombre': 'The Matrix',
                'director': 'Lana y Lilly Wachowski',
                'año': 1999,
                'edad': '+16 años',
                'edad_minima': 16,
                'imagen': 'images/matrix.svg',
                'sinopsis': 'Un programador y hacker descubre que su mundo es una elaborada simulación virtual y lidera la rebelión de la resistencia humana contra las máquinas.',
                'destacada': True,
            },
            {
                'id': 3,
                'nombre': 'Blade Runner 2049',
                'director': 'Denis Villeneuve',
                'año': 2017,
                'edad': '+14 años',
                'edad_minima': 14,
                'imagen': 'images/blade_runner.svg',
                'sinopsis': 'Un blade runner desentierra un secreto oculto durante tres décadas que tiene el potencial de desatar el caos entre humanos y replicantes.',
                'destacada': False,
            },
        ],
    },
    'animacion': {
        'slug': 'animacion',
        'nombre': 'Animación',
        'icono': 'bi-palette-fill',
        'color': 'warning',
        'banner': 'El arte de la animación llevado a su máxima expresión visual y narrativa.',
        'descripcion': 'Obras de arte visual y narrativas conmovedoras que exploran mundos fantásticos, magia, leyendas y emociones universales para toda la familia.',
        'peliculas': [
            {
                'id': 4,
                'nombre': 'Spider-Man: Into the Spider-Verse',
                'director': 'Peter Ramsey, Bob Persichetti, Rodney Rothman',
                'año': 2018,
                'edad': '+7 años / TE',
                'edad_minima': 7,
                'imagen': 'images/spider_verse.svg',
                'sinopsis': 'El joven Miles Morales es picado por una araña radiactiva y aprende a ser Spider-Man con la ayuda de versiones alternas del héroe multiversal.',
                'destacada': True,
            },
            {
                'id': 5,
                'nombre': 'Coco',
                'director': 'Lee Unkrich, Adrián Molina',
                'año': 2017,
                'edad': 'Todo Espectador',
                'edad_minima': 0,
                'imagen': 'images/coco.svg',
                'sinopsis': 'Miguel, un niño apasionado por la música, emprende un viaje extraordinario a la mágica Tierra de los Muertos para descubrir el misterio de su familia.',
                'destacada': True,
            },
            {
                'id': 6,
                'nombre': 'El Viaje de Chihiro',
                'director': 'Hayao Miyazaki',
                'año': 2001,
                'edad': 'Todo Espectador',
                'edad_minima': 0,
                'imagen': 'images/el_viaje_de_chihiro.svg',
                'sinopsis': 'Chihiro es una niña de diez años que queda atrapada en un mundo gobernado por dioses, brujas y espíritus, y debe rescatar a sus padres convertidos en cerdos.',
                'destacada': False,
            },
        ],
    },
}


def inicio(request):
    generos_lista = list(CATALOGO_GENEROS.values())
    total_peliculas = sum(len(g['peliculas']) for g in generos_lista)

    context = {
        'titulo': 'Catálogo de Películas',
        'alumno': 'Benjamín Rivas',
        'generos': generos_lista,
        'total_peliculas': total_peliculas,
        'total_generos': len(generos_lista),
    }
    return render(request, 'inicio.html', context)


def detalle_genero(request, slug_genero):
    if slug_genero not in CATALOGO_GENEROS:
        raise Http404("Género no encontrado")

    genero = CATALOGO_GENEROS[slug_genero]
    otros_generos = [g for slug, g in CATALOGO_GENEROS.items() if slug != slug_genero]

    context = {
        'titulo': f"Películas de {genero['nombre']}",
        'genero': genero,
        'peliculas': genero['peliculas'],
        'otros_generos': otros_generos,
        'alumno': 'Benjamín Rivas',
    }
    return render(request, 'genero.html', context)
