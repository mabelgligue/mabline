import pyowm

apiKey = '3c9eaf32882bfec545d09bbaaf1e59e8'
#apiKey ='{}'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place('Koforidua,Ghana')

w = observation.get_weather()
 
w.get_wind()
w.get_humidity()
w.get_temperature()

print(w.get_humidity())
print(w.get_temperature())
print(w.get_wind())
