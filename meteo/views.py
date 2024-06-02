from django.shortcuts import render
import requests
import json
from .models import Cidade, Previsao
from datetime import datetime, date

# Create your views here.

def index_view(request):
    forecast_url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    weather_types_url = 'http://api.ipma.pt/open-data/weather-type-classe.json'

    try:
        forecast_response = requests.get(forecast_url)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        weather_types_response = requests.get(weather_types_url)
        weather_types_response.raise_for_status()
        weather_types_text = weather_types_response.text
        weather_types_data = json.loads(weather_types_text)

        forecast_today = forecast_data['data'][0]
        min_temp = forecast_today['tMin']
        max_temp = forecast_today['tMax']
        forecast_date = forecast_today['forecastDate']
        id_weather_type = forecast_today['idWeatherType']

        if isinstance(weather_types_data, dict) and 'data' in weather_types_data:
            weather_description = "Descrição indisponível"
            for item in weather_types_data['data']:
                if item.get('idWeatherType') == id_weather_type:
                    weather_description = item.get('descIdWeatherTypePT', 'Descrição indisponível')
                    break
        else:
            raise ValueError("A resposta da API para as classes de tempo não está no formato esperado.")

        icon_name = f"w_ic_d_{id_weather_type:02}anim.svg"
        icon_path = f"meteo/{icon_name}"
    except requests.exceptions.RequestException as e:
        min_temp = "N/A"
        max_temp = "N/A"
        forecast_date = "N/A"
        weather_description = "Descrição indisponível"
        icon_path = "meteo/default_icon.svg"  # Definir um ícone padrão para o caso de erro
    except Exception as e:
        min_temp = "N/A"
        max_temp = "N/A"
        forecast_date = "N/A"
        weather_description = "Descrição indisponível"
        icon_path = "meteo/default_icon.svg"
        print(f"Erro ao processar a resposta da API: {e}")

    context = {
        'forecast_date': forecast_date,
        'min_temp': min_temp,
        'max_temp': max_temp,
        'weather_description': weather_description,
        'icon_path': icon_path
    }

    return render(request, 'meteo/index.html', context)

def prevlist_view(request):
    distritos_islands_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    distritos_islands_response = requests.get(distritos_islands_url)
    distritos_islands_data = distritos_islands_response.json()['data']

    for cidade in Cidade.objects.all():
        cidade_info = next((item for item in distritos_islands_data if item['local'] == cidade.name), None)
        if cidade_info:
            ipma_id = cidade_info.get('globalIdLocal')
            if ipma_id:
                forecast_url = f"http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{ipma_id}.json"
                forecast_response = requests.get(forecast_url)
                forecast_data = forecast_response.json()

                main_forecast = forecast_data['data'][0]
                main_data = datetime.strptime(main_forecast['forecastDate'], '%Y-%m-%d').date()
                main_temp_min = main_forecast['tMin']
                main_temp_max = main_forecast['tMax']
                id_weather_type = main_forecast['idWeatherType']
                wtid = f"{id_weather_type:02}"

                main_previsao, created = Previsao.objects.get_or_create(
                    cidade=cidade, data=main_data,
                    defaults={'temp_min': main_temp_min, 'temp_max': main_temp_max, 'previsoes': None, 'wtid':wtid}
                )

                if created:
                    for forecast in forecast_data['data'][1:6]:
                        data = datetime.strptime(forecast['forecastDate'], '%Y-%m-%d').date()
                        temp_min = forecast['tMin']
                        temp_max = forecast['tMax']
                        forecast_weather_type = forecast['idWeatherType']
                        wtid_forecast = f"{forecast_weather_type:02}"

                        Previsao.objects.create(
                            cidade=cidade, data=data, temp_min=temp_min, temp_max=temp_max, previsoes=main_previsao, wtid=wtid_forecast
                        )

    main_previsoes = Previsao.objects.filter(previsoes__isnull=True).prefetch_related('prevs')

    return render(request, 'meteo/prevlist.html', {'main_previsoes': main_previsoes})

