from openai import OpenAI

client = OpenAI(api_key='YOUR-APIKEY')
print("AIとチャットを始めます。"
      "チャットを終了するときは、exit() と入力してください。")
#　チャットの履歴を保存するリスト
messages = []

while True:
    #プロンプトを入力する
    user_prompt = input('あなた: ')

    if user_prompt == 'exit()':
        break
    #チャットの履歴にプロンプトを追加
    messages.append({"role":"user", "content":user_prompt})

    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=messages)
    content = response.choices[0].message
    print("AI: ", content.content)

    #チャットの履歴に追加する
    messages.append({"role": content.role,"content": content.content})