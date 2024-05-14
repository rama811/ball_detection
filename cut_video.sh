#!/bin/bash

# Argumentos
input_video="$1"
start_time="$2"
end_time="$3"

# Ejecuta el script de Python con los argumentos proporcionados
python3 cut_video.py "$input_video" "$start_time" "$end_time"