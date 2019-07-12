import pyowm
apiKey = ""
 owm = pyowm.OWM(apiKey)
 observation = owm.weather_at_place('london,uk')
 w = observation.get_weather()
 
 w.get_wind()
 w.get_humidity()