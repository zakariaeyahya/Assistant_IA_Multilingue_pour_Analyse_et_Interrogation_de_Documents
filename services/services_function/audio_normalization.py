# File: services/services_function/audio_normalization.py

import numpy as np

def normalize_audio(audio_array):
    if audio_array.size == 0:
        return np.array([], dtype=np.int16)

    # Ensure audio is mono
    if len(audio_array.shape) > 1 and audio_array.shape[0] > 1:
        audio_array = np.mean(audio_array, axis=0)
    
    # Avoid division by zero
    max_abs_val = np.max(np.abs(audio_array))
    if max_abs_val == 0:
        return np.zeros(audio_array.shape, dtype=np.int16)

    # Normalize to [-1, 1] range
    audio_array = audio_array / max_abs_val
    
    # Convert to int16 range
    audio_array_int16 = (audio_array * 32767).astype(np.int16)
    
    return audio_array_int16