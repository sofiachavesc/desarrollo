import assemblyai as aai

# Configura tu API Key de AssemblyAI
aai.settings.api_key = "f36180a9abaf4f21bed218bc722bd747"

# Archivo de audio local
audio_file = "C:\\Users\\sofia\\Desktop\\actas bot\\4. Grabacion de Audio Palmar de la Ciénaga.mp3"

# Configuración de la transcripción
config = aai.TranscriptionConfig(
    language_code="es",  # Especifica el idioma español
    speaker_labels=True,  # Habilita etiquetas de hablantes
    summarization=False   # Asegura que no se genere un resumen
)

# Función principal para transcribir
def transcribir_audio(file_path):
    try:
        # Inicializa el transcriptor
        transcriber = aai.Transcriber()

        # Procesa el archivo local
        transcript = transcriber.transcribe(file_path, config)

        # Verifica el estado de la transcripción
        if transcript.status == aai.TranscriptStatus.error:
            print(f"Error en la transcripción: {transcript.error}")
            exit(1)

        # Imprime la transcripción completa
        print("Transcripción completada:")
        print(transcript.text)

        # Imprime cada intervención de los hablantes
        print("\nIntervenciones de los hablantes:")
        for utterance in transcript.utterances:
            print(f"Speaker {utterance.speaker}: {utterance.text}")

    except Exception as e:
        print(f"Error: {e}")

# Llamada al flujo principal
if __name__ == "__main__":
    transcribir_audio(audio_file)
