from django.db import migrations, models
import requests
from bs4 import BeautifulSoup

def load_data(apps, schema_editor):
    
    """Función para obtener el contenido de la página https://www.scrapethissite.com/pages/simple/"""
    
    # Carga del modelo de la base de datos
    Pais = apps.get_model('base', 'Pais')
    
    # Conexión al sitio web
    response = requests.get("https://www.scrapethissite.com/pages/simple/")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Busca todos los elementos de la clase country en el html
    countries = soup.find_all('div', class_='country')

    # Ciclo para iterar sobre cada country encontrado y añadir la infomacion a la base de datos
    for country in countries:
        nombre = country.find('h3').text.strip()
        capital = country.find('span', class_='country-capital').text
        population = int(country.find('span', class_='country-population').text)
        area = int(round(float(country.find('span', class_='country-area').text)))
            
        Pais.objects.create(nombre=nombre, capital=capital, poblacion=population, area=area)

def unload_data(apps, schema_editor):
    """Función para vovler a cargar los datos"""
    
    Pais = apps.get_model('base', 'Pais')
    Pais.objects.all().delete()
    
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        
        # Creación del modelo de la base de datos
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('poblacion', models.BigIntegerField()),
                ('area', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RunPython(load_data, reverse_code=unload_data), # Carga de los datos con la función load_data
    ]
