from pydub import AudioSegment
from pydub.effects import normalize

# Function to increase volume by a given amount (in dB)
def increase_volume(audio_file, db_increase=10):  # Moderate increase of 10dB
    sound = AudioSegment.from_file(audio_file)
    louder_sound = sound + db_increase  # Increase volume by specified dB
    louder_file = audio_file.replace(".m4a", "_louder.wav")
    louder_sound.export(louder_file, format="wav")
    return louder_file

# Function to normalize audio volume (makes quiet parts louder and loud parts quieter)
def normalize_audio(audio_file):
    sound = AudioSegment.from_file(audio_file)
    normalized_sound = normalize(sound)  # Normalize audio volume
    normalized_file = audio_file.replace(".m4a", "_normalized.wav")
    normalized_sound.export(normalized_file, format="wav")
    return normalized_file

# Function to apply equalization (boosts human speech frequencies)
def apply_equalization(audio_file):
    sound = AudioSegment.from_file(audio_file)
    equalized_sound = sound.low_pass_filter(4000).high_pass_filter(1000)  # Boost human speech frequencies
    equalized_file = audio_file.replace(".m4a", "_equalized.wav")
    equalized_sound.export(equalized_file, format="wav")
    return equalized_file

# Master function to apply all or selected refining steps to an audio file
def refine_audio(audio_file, apply_volume=True, apply_normalize=True, apply_equalize=True, apply_resample=False):
    refined_file = audio_file

    # Step 1: Increase Volume
    if apply_volume:
        print("Increasing volume...")
        refined_file = increase_volume(refined_file)

    # Step 2: Normalize Audio
    if apply_normalize:
        print("Normalizing audio...")
        refined_file = normalize_audio(refined_file)

    # Step 3: Apply Equalization
    if apply_equalize:
        print("Applying equalization...")
        refined_file = apply_equalization(refined_file)

    print(f"Refined audio saved as: {refined_file}")
    return refined_file

# Example usage
if __name__ == "__main__":
    # Specify the path to your audio file (must be in .m4a format for this example)
    audio_file_path = r""

    # Apply refining steps with moderate volume increase, normalization, and equalization
    refined_audio = refine_audio(audio_file_path, apply_volume=True, apply_normalize=True, apply_equalize=True, apply_resample=False)
