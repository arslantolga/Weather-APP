import tkinter
from io import BytesIO
import requests
from PIL import Image, ImageTk

def search():
    city = city_entry.get()

    url_weather = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b621d2fc2cbed7afe6c33cbfce06fb0c&lang=tr'
    response_weather = requests.get(url_weather)

    icon_id = response_weather.json()["weather"][0]["icon"]
    url_icon = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'

    image_data = requests.get(url_icon).content
    image = Image.open(BytesIO(image_data))
    image_tk = ImageTk.PhotoImage(image)

    image_label.config(image=image_tk, bg="light blue")
    image_label.image = image_tk

    description = response_weather.json()["weather"][0]["description"]
    temp = response_weather.json()["main"]["temp"] - 273.15
    temp_min = response_weather.json()["main"]["temp_min"] - 273.15
    temp_max = response_weather.json()["main"]["temp_max"] - 273.15
    humidity = response_weather.json()["main"]["humidity"]
    country = response_weather.json()["sys"]["country"]
    name = response_weather.json()["name"]

    text = f"""
    Country : {country.capitalize()}
    City : {name.capitalize()}
    Description : {description.capitalize()}
    Temperature : {round(temp, 2)}°C
    Max Temperature : {round(temp_max, 2)}°C
    Min Temperature : {round(temp_min, 2)}°C
    Humidity : {humidity}%
    """

    result_label.config(text=text)


FONT = ("Arial", 15, "bold")

window = tkinter.Tk()
window.geometry("500x800")
window.title("My Weather APP")
window.config(bg="light blue")

app_logo = ImageTk.PhotoImage(Image.open("weather.png"))

empty_label = tkinter.Label(text="", pady=0.5, bg="light blue")
empty_label.pack()

app_log_label = tkinter.Label(image=app_logo, bg="light blue")
app_log_label.pack()

empty_label = tkinter.Label(text="", pady=0.1, bg="light blue")
empty_label.pack()

city_label = tkinter.Label(text="Enter Your City", font=FONT, bg="light blue")
city_label.pack()

empty_label = tkinter.Label(text="", pady=0.1, bg="light blue")
empty_label.pack()

city_entry = tkinter.Entry()
city_entry.pack()

empty_label = tkinter.Label(text="", pady=0.1, bg="light blue")
empty_label.pack()

search_button = tkinter.Button(text="Search", font=("Arial", 10, "bold"), bg="light blue", command=search)
search_button.pack()

empty_label = tkinter.Label(text="", pady=0.1, bg="light blue")
empty_label.pack()

image_label = tkinter.Label(text="", bg="light blue")
image_label.pack()

result_label = tkinter.Label(text="", font=("Halvetica", 15, "italic"), bg="light blue", justify="left")
result_label.pack()

window.mainloop()
