
import requests
import smtplib

from appier import email_parts

MY_EMAIL = os.environ.get(OMW_MY_EMAIL)
PASSWORD = os.environ.get(OMW_PASSWORD)





api_key = os.environ.get(OMW_API_KEY)
lat = 33.28
lon = -81.37
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
weather_params = {
    'lat':lat
    ,'lon':lon,
    'appid':api_key
    ,'cnt':4
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
message = "Bring an umbrella"




def is_it_raining():
    rain_list = []
    for hour_data in weather_data['list']:
        condition = hour_data['weather'][0]['id']
        if condition < 700:
            rain_list.append(condition)
    if len(rain_list) > 0:
        return True
    else:
        return False

if is_it_raining():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='matthewsinquefield@gmail.com',
                            msg=f"Subject:Rain Ahead!\n\n{message}"
                            )
