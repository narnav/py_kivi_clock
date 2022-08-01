import requests
import kivy
kivy.require('1.0.7')
import json
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from functools import partial
from kivy.clock import Clock

def my_callback(value, key, *largs):
    # def animate(self, instance):
    # read data from API (crypto)
    x = requests.get('https://www.deribit.com/api/v2/public/get_index_price?index_name=eth_usd')
    # convert from string to JSON object
    y = json.loads(x.text)

    # test print
    print(y)
    print(y["result"]["index_price"])
    # saev data to local variable
    price= y["result"]["index_price"]

    # Opening JSON file (read history)
    f = open('sample.json')

    # save all data to file
    data = json.load(f)
    data.append({"price": price})
    json_object = json.dumps(data, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)


Clock.schedule_interval(partial(my_callback, 'my value', 'my key'), 2)

class TestApp(App):

    def animate(self, instance):
        # read data from API (crypto)
        x = requests.get('https://www.deribit.com/api/v2/public/get_index_price?index_name=eth_usd')
        # convert from string to JSON object
        y = json.loads(x.text)

        # test print
        print(y)
        print(y["result"]["index_price"])
        # saev data to local variable
        price= y["result"]["index_price"]

        # Opening JSON file (read history)
        f = open('sample.json')
  
        # save all data to file
        data = json.load(f)
        data.append({"price": price})
        json_object = json.dumps(data, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    def build(self):
        button = Button(size_hint=(None, None), text='plop',on_press=self.animate)
        return button


if __name__ == '__main__':
    TestApp().run()