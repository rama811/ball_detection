import os
import cv2

def export_frames(video_path, output_folder):
    # Verifica si la carpeta de salida existe, si no existe la crea
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Abre el video
    video = cv2.VideoCapture(video_path)

    # Verifica si el video se abrió correctamente
    if not video.isOpened():
        print("Error al abrir el video.")
        return

    # Contador de frames
    frame_count = 0

    # Itera sobre cada frame del video
    while True:
        # Lee el siguiente frame
        ret, frame = video.read()

        # Verifica si se pudo leer el frame
        if not ret:
            break

        # Guarda el frame como imagen
        frame_path = f"{output_folder}/frame_{frame_count:04d}.jpg"
        print(frame_path)
        cv2.imwrite(frame_path, frame)

        # Incrementa el contador de frames
        frame_count += 1

    # Cierra el video
    video.release()

# Nombre del video
video_name = 'Real_Madrid_vs_Barcelona_2016_2017_acortado'

# Ruta del video de entrada
video_path = f"video_test/{video_name}.mp4"

# Carpeta de salida para las imágenes
output_folder = f"dataset/{video_name}/frames"

# Exporta los frames del video como imágenes
export_frames(video_path, output_folder)