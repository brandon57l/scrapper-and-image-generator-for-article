import os
import webbrowser
import openai

secret = ''

prompt = input("Prompt= ")

openai.api_key = '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' # your api key
# openai.Model.list()

def create():
    res = openai.Image.create(
    prompt=prompt,
        n=2,
        size="1024x1024"
    )
    url = res["data"][0]['url']

    webbrowser.open_new_tab(url)

def variation():
    res = openai.Image.create_variation(
        image=open("vincent.png", "rgb"),
        n=1,
        size="512x512"
    )
    url = res['data'][0]['url']

    webbrowser.open_new_tab(url)

create()