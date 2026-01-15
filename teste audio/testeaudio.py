import yt_dlp

link = input('Digite ou cole o link do video que deseja baixar: ')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': r'C:\ffmpeg\ffmpeg-8.0.1-essentials_build\bin',
    'quiet': False,
    'no_warnings': False,
    'restrictfilenames': True,
    'no_color': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print('Baixando...')
    info = ydl.extract_info(link, download=True)
    print(f'Download concluído: {info["title"]}')


