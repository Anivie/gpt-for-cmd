import openai
import os
from colorama import Fore, Style
import json

my_msg = []


def ask_gpt(prompt):
    my_msg.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=my_msg
    )
    answers = response['choices'][0]['message']['content']
    my_msg.append({"role": response['choices'][0]['message']['role'], "content": answers})
    return answers


if __name__ == '__main__':
    openai.api_key = os.getenv('OPENAI_KEY')

    while True:
        question = input('输入问题：')
        if question.startswith('_'):
            if question == '_stop':
                break
            if question == '_clear':
                my_msg.clear()
                os.system('cls')
                continue
            if question == '_export':
                with open("C:/Users/anivi/OneDrive/桌面/gpt_export.txt", "w") as f:
                    json.dump(my_msg, f, ensure_ascii=False, indent=4)
                continue
            print("No command found.")
        else:
            answer = ask_gpt(question)
            print(answer)
            print(Fore.GREEN + '\n===========================END===========================\n' + Style.RESET_ALL)
