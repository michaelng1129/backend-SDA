import speech
from flask import Flask, jsonify, request
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/', methods=['GET', 'POST'])
def run():
    # print(request.json)
    # print(request.json['speech_base64_data'])
    option = 0
    img_option = 0
    if 'img_base64_data' in request.json:
        img_base64_data = request.json['img_base64_data']
        print(img_base64_data)
        img_option = 1
        ans = base64.b64decode(img_base64_data)
        out = open('./Resource/userFace.bmp', 'wb')
        out.write(ans)
        out.close()
    if 'speech_base64_data' in request.json:
        speech_base64_data = request.json['speech_base64_data']
        print(speech_base64_data)
        print('hello')
        ans = base64.b64decode(speech_base64_data)
        out = open('./Resource/speech.wav', 'wb')
        out.write(ans)
        out.close()

    # only add a file named Text.txt and add ↓ these codes
    if 'text_data' in request.json:
        option = 1
        text_string_data = request.json['text_data']
        print(text_string_data)
        out = open('./Resource/Text.txt', 'w')
        out.write(text_string_data)
        out.close()
    #Start Process
    if option:
        speech.Text_To_Animation(img_option)
    else:
        speech.Speech_To_Animation(img_option)

    # end
    ToBase64('./Resource/right.mp4', './Resource/base64Right.txt')
    ToBase64('./Resource/wrong.mp4', './Resource/base64Wrong.txt')
    # ToFile('ans.txt', 'ans2.mp4')
    with open('./Resource/base64Right.txt', 'rb') as fileObj:
        base64_data = fileObj.read()
    with open('./Resource/base64Wrong.txt', 'rb') as fileObj:
        base64_data2 = fileObj.read()
    print(base64_data)
    print(base64_data2)
    if option:
        return jsonify({
            'video_generated': 'data:video/mp4;base64,'+str(base64_data)[2:-1]
        })
    else:
        return jsonify({
            'video_generated': 'data:video/mp4;base64,'+str(base64_data)[2:-1],
            'video_generated2': 'data:video/mp4;base64,'+str(base64_data2)[2:-1]
        })

def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()

def ToFile(txt, file):
    with open(txt, 'rb') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

#ToBase64('ans.mp4', 'ans.txt')
#ToFile('ans.txt', 'ans2.mp4')
# ToFile('speech.txt', 'speech.mp4')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
