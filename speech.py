import os, sda
import azure.cognitiveservices.speech as speechsdk
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def Speech_To_Animation(img_option):
    speech_key, service_region = "0cb1662358a74aa59c07ed47f04050a7", "eastasia"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    speech_filename = './Resource/speech.wav'
    audio_config = speechsdk.audio.AudioConfig(filename=speech_filename)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    STT_result = speech_recognizer.recognize_once()
    if STT_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(STT_result.text))
    elif STT_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif STT_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = STT_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    print("STT Done.")

    #voice = "Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)"
    voice = "en-US-GuyNeural"
    speech_config.speech_synthesis_voice_name = voice
    file_name = "./Resource/rightAudio.wav"
    if os.path.exists(file_name):
        os.remove(file_name)
    file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)
    result = speech_synthesizer.speak_text_async(STT_result.text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(STT_result.text, file_name))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    print("TTS Done.")

    va = sda.VideoAnimator(model_path="timit")# Instantiate the animator
    if img_option:
        source_path = "Resource/userFace.bmp"
    else:
        source_path = "Resource/speaker1.bmp"
    vid, aud = va(source_path, "./Resource/rightAudio.wav")
    va.save_video(vid, aud, "./Resource/right.mp4")
    vid, aud = va(source_path, "./Resource/speech.wav")
    va.save_video(vid, aud, "./Resource/wrong.mp4")
    print("SDA Done.")

def Text_To_Animation(img_option):
    speech_key, service_region = "0cb1662358a74aa59c07ed47f04050a7", "eastasia"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    with open("./Resource/Text.txt", "r") as fileObj:
        content = fileObj.read()
    #voice = "Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)"
    voice = "en-US-GuyNeural"
    speech_config.speech_synthesis_voice_name = voice
    file_name = "./Resource/rightAudio.wav"
    if os.path.exists(file_name):
        os.remove(file_name)
    file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)
    result = speech_synthesizer.speak_text_async(content).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(content, file_name))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    print("TTS Done.")

    va = sda.VideoAnimator(model_path="timit")# Instantiate the animator
    if img_option:
        source_path = "Resource/userFace.bmp"
    else:
        source_path = "Resource/speaker1.bmp"
    vid, aud = va(source_path, "./Resource/rightAudio.wav")
    va.save_video(vid, aud, "./Resource/right.mp4")
    vid, aud = va(source_path, "./Resource/speech.wav")
    va.save_video(vid, aud, "./Resource/wrong.mp4")
    print("SDA Done.")