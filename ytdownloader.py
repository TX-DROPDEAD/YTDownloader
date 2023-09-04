from pytube import YouTube
from tqdm import tqdm
import requests
import os

def clean_filename(filename):
    # Elimina caracteres inválidos del nombre del archivo
    valid_chars = '-_() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(char for char in filename if char in valid_chars)

def Download(link):
    youtubeObject = YouTube(link)
    stream = youtubeObject.streams.get_highest_resolution()
    video_title = clean_filename(youtubeObject.title)
    file_size = stream.filesize

    with open(f'{video_title}.mp4', 'wb') as file, tqdm(
        total=file_size, 
        unit='B', 
        unit_scale=True, 
        unit_divisor=1024,
        ncols=100,
        bar_format="{l_bar}{bar}{r_bar}",
    ) as bar:
        response = requests.get(stream.url, stream=True)
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            bar.update(len(data))

    print("\nDescarga completada con éxito")

while True:
    link = input("Ingresa la URL del video de YouTube: ")
    Download(link)
    respuesta = input("¿Deseas descargar otro video? (Sí/No): ")
    if respuesta.lower() != 'si':
        break





