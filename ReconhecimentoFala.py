
import speech_recognition as sr
import nltk

# Baixe os recursos necessários do NLTK
nltk.download('punkt')

def transcrever_audio(audio_file):
    recognizer = sr.Recognizer()

    # Carrega o áudio
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    # Usa o reconhecedor de fala para transcrever o áudio
    try:
        transcript = recognizer.recognize_google(audio_data, language='pt-BR')
        return transcript
    except sr.UnknownValueError:
        return "Não foi possível entender o áudio"
    except sr.RequestError as e:
        return f"Erro na requisição ao Google Speech Recognition: {e}"

def verificar_acerto(transcript, texto_referencia):
    words_transcript = nltk.word_tokenize(transcript.lower())
    words_reference = nltk.word_tokenize(texto_referencia.lower())

    # Calcula a precisão das palavras reconhecidas comparadas ao texto de referência
    correct_words = [word for word in words_transcript if word in words_reference]
    accuracy = (len(correct_words) / len(words_reference)) * 100

    return accuracy

# Texto de referência para verificar a precisão
#texto_referencia = "O menino quer um burrinho pra passear. Um burrinho manso, que não corra nem pule, mas que saiba conversar."
texto_referencia = "O menino quer um burrinho pra passear Um burrinho manso que não corra nem pule mas que saiba conversar"

# Nome do arquivo de áudio gravado que você deseja transcrever
#Leitura incorreta
audio_file = "teste1.wav"
#Leitura correta
#audio_file = "teste2.wav"

# Transcreve o áudio
transcricao = transcrever_audio(audio_file)

# Verifica a precisão das palavras reconhecidas
precisao = verificar_acerto(transcricao, texto_referencia)

print("Transcrição do áudio:", transcricao)
print("Precisão das palavras reconhecidas:", precisao, "%")
