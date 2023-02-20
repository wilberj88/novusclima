# Weather Alerts: https://python.plainenglish.io/10-mini-automation-scripts-for-everyday-python-projects-e69396640d60

# pip install pywttr
# pip install windows-toasts
from pywttr import Wttr
from windows_toasts import WindowsToaster, ToastText1
# Get weather data
city = "London"
weather = Wttr(city)
w = weather.en()
# Show weather alert
notifier = WindowsToaster("Weather Alert")
msg = ToastText1()
msg.SetBody(w.weather[0].avgtemp_c + "°C")
msg.on_activated = lambda action: print(action)
notifier.show_toast(msg)
