from banglatts import BanglaTTS



def speech_reply(text, voice='female'):
    tts = BanglaTTS(save_location="save_model_location")

    # wave = tts(
    #     text, voice=voice,
    #     filename=TEMP_AUDIO,
    #     convert_type="file"
    # )  # voice can be male or female
    # tts = BanglaTTS(save_location="save_model_location")
    wave = tts(
        text, voice=voice,
        # filename=TEMP_AUDIO,
        convert_type="numpy"
    )  # voice can be male or female
    return wave
    # sd.play(wave, blocking=True)


if __name__ == '__main__':
    speech_reply("এবাংলায় কথা বলতে পান্ড।")
    speech_reply("এবাংলায় কথা বলতে পান্ড।")
