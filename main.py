import googletrans


import codecs
import csv
import sys
import random
import deepl
import openai

auth_key = "4185f113-e656-7c12-e167-21e5b8b578d8:fx"
googtranslator = googletrans.Translator()


deepTranslator = deepl.Translator(auth_key)
openai.api_key = "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"




if len(sys.argv) != 3:
        sys.exit("Usage: translate.py FILENAME OUTPUTNAME")

input = sys.argv[1]

outputname = str(sys.argv[2])
# outputname = "test"

outputname = outputname + ".txt"

o = open(outputname, "a", encoding="utf8")

with open(input, encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        line = line.strip().strip('/"').strip("”").strip("\n")
        print(line)
        if line:
            o.write(line)
            prompt_text = f"Translate the following Korean sentence into English: \"{line}\""

            # Make a call to the OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-003",  # As of April 2023, replace with the latest model if there's a new one
                prompt=prompt_text,
                temperature=0.3,  # A lower temperature makes the translation more literal and less creative
                max_tokens=60,  # Adjust as needed based on the length of the translation
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            openAi_translation = response.choices[0].text.strip()
            google_translation = googtranslator.translate(line, dest="en").text
            deepLearning_translation = deepTranslator.translate_text(line, target_lang="EN-US").text
            print(f"OpenAi Translation : {openAi_translation}")
            print(f"Google Translation : {google_translation}")
            print(f"DeepL Translation : {deepLearning_translation}")
            o.write(openAi_translation + "\n")
            o.write(google_translation + "\n")
            o.write(deepLearning_translation + "\n")