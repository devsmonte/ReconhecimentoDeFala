import speech_recognition as sr
import nltk

# Baixe os recursos necessários do NLTK
nltk.download('punkt')

# Função para transcrever o áudio
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

# Função para calcular palavras por minuto (PPM)
def calcular_palavras_por_minuto(transcricao, duracao_segundos):
    palavras = nltk.word_tokenize(transcricao.lower())
    total_palavras = len(palavras)
    duracao_minutos = duracao_segundos / 60
    ppm = total_palavras / duracao_minutos if duracao_minutos > 0 else 0
    return ppm

# Função para avaliar a fluência
def avaliar_fluencia(transcricao, texto_referencia):
    words_transcript = nltk.word_tokenize(transcricao.lower())
    words_reference = nltk.word_tokenize(texto_referencia.lower())

    # Calcula a quantidade de palavras corretamente transcritas
    corretas = [word for word in words_transcript if word in words_reference]
    percentual_acerto = (len(corretas) / len(words_reference)) * 100 if len(words_reference) > 0 else 0

    # Avalia a fluência com base na precisão de pronúncia das palavras
    palavras_diferentes = set(words_reference)
    acertos_pronuncia = [word for word in palavras_diferentes if word in words_transcript]
    percentual_pronuncia = (len(acertos_pronuncia) / len(palavras_diferentes)) * 100 if len(palavras_diferentes) > 0 else 0

    return percentual_acerto, percentual_pronuncia

# Texto de referência para verificar a precisão
texto_referencia = "O menino quer um burrinho pra passear Um burrinho manso que não corra nem pule mas que saiba conversar"

# Nome do arquivo de áudio gravado que você deseja transcrever
#Correto
audio_file = "D:\Pessoal\\Academico\\SOFTEX\\ReconhecimentoDeFala\\teste2.wav"
#Errado
#audio_file = "D:\Pessoal\\Academico\\SOFTEX\\ReconhecimentoDeFala\\teste1.wav"

# Transcreve o áudio
transcricao = transcrever_audio(audio_file)

# Obtém a duração do áudio (substitua pela duração real do áudio em segundos)
duracao_audio_segundos = 9  # Por exemplo, 5 minutos

# Calcula as palavras por minuto (PPM)
ppm = calcular_palavras_por_minuto(transcricao, duracao_audio_segundos)

# Avalia a fluência
acerto, pronuncia = avaliar_fluencia(transcricao, texto_referencia)

# Imprime os resultados
print("Transcrição do áudio:", transcricao)
print("Palavras por minuto:", ppm)
print("Percentual de acerto de palavras:", acerto, "%")
print("Percentual de pronúncia correta de palavras:", pronuncia, "%")