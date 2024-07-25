from gtts import gTTS
import os
import json



# Load phrases from JSON file
with open('phrases.json', 'r', encoding='utf-8') as f:
    phrases = json.load(f)

if not os.path.exists('audio'):
    os.makedirs('audio')

error_log = []

# Generate audio files for each Polish phrase
for phrase in phrases:
    word = phrase['polish']
    try:
        tts = gTTS(text=word, lang='pl')
        tts.save(f"audio/{word}.mp3")
        print(f"Generated audio for: {word}")
    except Exception as e:
        error_log.append({'phrase': word, 'error': str(e)})
        print(f"Error generating audio for: {word}, Error: {str(e)}")

# Write errors to a log file
if error_log:
    with open('error_log.txt', 'w', encoding='utf-8') as log_file:
        for error in error_log:
            log_file.write(f"Phrase: {error['phrase']}, Error: {error['error']}\n")

print("Audio generation completed with errors logged.")
