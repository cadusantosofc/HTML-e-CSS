from pytube import YouTube
from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog

# Cria uma janela tkinter para o usuário selecionar onde salvar o arquivo
root = tk.Tk()
root.withdraw()
save_path = filedialog.askdirectory()

# Solicita ao usuário que insira o link do vídeo
video_url = input("Digite o link do vídeo do YouTube: ")

# Obtém o vídeo com a melhor resolução e o baixa
yt = YouTube(video_url)
ys = yt.streams.get_highest_resolution()

# Define o nome do arquivo a ser salvo
filename = yt.title + ".mp4"

# Baixa o vídeo no diretório selecionado pelo usuário
ys.download(save_path, filename=filename)
print('Video Baixado ...')

# Converte o vídeo baixado em um arquivo de áudio MP3
clip = VideoFileClip(save_path + '/' + filename)
audio_filename = yt.title + ".mp3"
clip.audio.write_audiofile(save_path + '/' + audio_filename)
print('Audio Baixado ...')

# Exibe uma mensagem de conclusão
print('Fechando Script <3 ...')
