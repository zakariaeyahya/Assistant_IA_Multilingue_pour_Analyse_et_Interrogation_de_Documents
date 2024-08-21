# File: services/services_function/audio_conversion.py

import subprocess
import logging
import os

logger = logging.getLogger(__name__)

def convert_opus_to_wav(opus_path, ffmpeg_path):
    logger.info(f"Converting opus to wav: {opus_path}")
    if not os.path.isfile(opus_path):
        logger.error(f"File not found: {opus_path}")
        return None
    
    if not os.path.isfile(ffmpeg_path):
        logger.error(f"FFmpeg executable not found: {ffmpeg_path}")
        return None

    wav_path = opus_path.rsplit('.', 1)[0] + '.wav'
    try:
        subprocess.run([ffmpeg_path, '-y', '-i', opus_path, wav_path], check=True)
        logger.info(f"Conversion successful: {wav_path}")
        return wav_path
    except subprocess.CalledProcessError as e:
        logger.error(f"Error during conversion: {e}")
        return None