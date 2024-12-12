import ChatTTS
import torchaudio
import torch

import os
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "2"
import gradio as gr


with gr.Blocks() as demo:
    gr.Markdown(
        """# 高风险需求实现-测试版
## 视频处理
 - [ ] 视频去水印
 - [ ] 视频去字幕
## 视频优化
 - [ ] 视频加字幕
 - [ ] 文案生成
 - [x] 文字生成语音
 """
    )

    with gr.Tab("视频处理"):
        with gr.Tab("视频去水印"):
            # TODO: add video watermark removal
            def VideoWatermarkRemoval(video):
                return video

            inp = gr.Video(label="上传视频")
            out = gr.Video(label="生成视频", show_download_button=True)
            sub = gr.Button("视频去水印")
            sub.click(VideoWatermarkRemoval, inputs=inp, outputs=out)
            pass
        with gr.Tab("视频去字幕"):
            # TODO: add video subtitle removal
            def VideoSubtitleRemoval(video):
                return video

            inp = gr.Video(label="上传视频")
            out = gr.Video(label="生成视频", show_download_button=True)
            sub = gr.Button("视频去字幕")
            sub.click(VideoSubtitleRemoval, inputs=inp, outputs=out)

            pass
    with gr.Tab("视频优化"):
        with gr.Tab("视频生成字幕"):
            # TODO: add video captioning
            def VideoCaptioning(video):
                return video

            inp = gr.Video(label="上传视频")
            out = gr.Video(label="生成视频", show_download_button=True)
            sub = gr.Button("字幕生成")
            sub.click(VideoCaptioning, inputs=inp, outputs=out)

            pass
        with gr.Tab("文案生成"):
            # TODO: add text generation
            def TongYiGen(title):
                return "【" + title + "】是一部好看的电影，值得一看。"

            inp = gr.Textbox(label="请输入文章标题")
            out = gr.Textbox(label="生成文案", lines=20, show_copy_button=True)
            sub = gr.Button("生成文案")
            sub.click(TongYiGen, inputs=inp, outputs=out)
            pass
        with gr.Tab("文字生成语音"):

            def test_audio_generation():
                notes = [
                    "C",
                    "C#",
                    "D",
                    "D#",
                    "E",
                    "F",
                    "F#",
                    "G",
                    "G#",
                    "A",
                    "A#",
                    "B",
                ]
                octave = 10
                note = 10
                duration = 1
                # fake generation
                sr = 48000
                a4_freq, tones_from_a4 = 440, 12 * (octave - 4) + (note - 9)
                frequency = a4_freq * 2 ** (tones_from_a4 / 12)
                duration = int(duration)
                audio = np.linspace(0, duration, duration * sr)
                audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(
                    np.int16
                )
                return sr, audio

            def Chatts_gen(text):

                # load model
                chat = ChatTTS.Chat()
                print(os.getcwd())
                chat.load(
                    source="custom", custom_path="../models/ChatTTS", compile=False
                )

                wavs = chat.infer([text])
                torchaudio.save(
                    "../output/audios/gradio_output_1.wav",
                    torch.from_numpy(wavs[0]).unsqueeze(0),
                    24000,
                )

                return 24000, wavs[0]

            inp = gr.Textbox(
                placeholder="输入文字",
                lines=10,
                label="请输入文本，最大350字左右",
                max_length=350,
            )
            out = gr.Audio(show_download_button=True)
            sub = gr.Button("生成语音")
            sub.click(Chatts_gen, inputs=inp, outputs=out)


if __name__ == "__main__":
    demo.launch()
