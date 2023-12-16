import pygame

from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from en_to_cn import to_cn
from cn_to_en import to_en
from audio_evaluation import audio_evaluation
from dialog import ask

def play_audio(file_path):
    pygame.mixer.init()  # 初始化音频引擎
    pygame.mixer.music.load(file_path)  # 载入音频文件
    pygame.mixer.music.play()  # 播放音频

if __name__ == "__main__":
    question =[]
    while(1):

        audio_file_name = 'oral_translation_en.pcm'

        # 语音识别
        audio_text = speech_to_text(audio_file_name)
        print('语音识别结果：', audio_text)

        aduio_score = audio_evaluation(audio_file_name, audio_text)
        print('语音评测得分是：', aduio_score)

        # 英翻中翻译
        _, audio_text_cn = to_cn(audio_text)
        print('翻译为中文得到：', audio_text_cn)

        # 输入模型得到回答
        question, ans_cn = ask(question, audio_text_cn)
        print("模型的回答是: ", ans_cn)

        # 中翻英
        _, audio_text_en = to_en(ans_cn)
        print('回答翻译为英文：', audio_text_en)

        # 播放英文
        text_to_speech(audio_text_en)

        audio_file_path = "./demo.wav"  # 替换为你的音频文件路径
        play_audio(audio_file_path)

        input("按 Enter 停止播放...")
        pygame.mixer.music.stop()  # 停止音频播放
        pygame.mixer.quit()  # 关闭音频引擎

        break

'''
if __name__ == "__main__":

    audio_file_name = 'oral_translation_en.pcm'
    # make_audio(audio_file_name)

    # 语音识别
    audio_text = speech_to_text(audio_file_name)
    print('打印出语音识别结果：', audio_text)

    aduio_score = audio_evaluation(audio_file_name, audio_text)
    print('语音评测得分是：', aduio_score)

    # 英翻中翻译
    _, audio_text_cn = to_cn(audio_text)
    print('打印出中文：', audio_text_cn)

    # 输入模型得到回答
    ans_cn = dialog(audio_text_cn)


    # 中翻英
    _, audio_text_en = to_en(ans_cn)
    print('打印出英文：', audio_text_en)

    # 播放英文
    text_to_speech(audio_text_en)

    audio_file_path = "./demo.wav"  # 替换为你的音频文件路径
    play_audio(audio_file_path)

    input("按 Enter 停止播放...")
    pygame.mixer.music.stop()  # 停止音频播放
    pygame.mixer.quit()  # 关闭音频引擎

    #print(audio_text)
'''
