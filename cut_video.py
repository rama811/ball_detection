from moviepy.editor import VideoFileClip

def acortar_video(input_video, output_video, start_time, end_time):
    # Carga el video
    video_clip = VideoFileClip(input_video)

    # Corta el video
    video_clip = video_clip.subclip(start_time, end_time)

    # Guarda el video acortado
    video_clip.write_videofile(output_video, codec="libx264", fps=24)

if __name__ == "__main__":
    # Ruta del video de entrada
    input_video = "Real_Madrid_vs_Barcelona_2016_2017.mp4"
    
    # Ruta del video de salida (video acortado)
    output_video = "Real_Madrid_vs_Barcelona_2016_2017_acortado.mp4"
    
    # Tiempo de inicio y final del video que deseas mantener
    start_time = 10*60  # segundos
    end_time = 11*60    # segundos

    # Llama a la función para acortar el video
    acortar_video(input_video, output_video, start_time, end_time)
