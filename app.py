 import subprocess
 import ffmpeg
 from ibm_watson import SpeechToTextV1
 from ibm_watson.websocket import RecognizeCallback, AudioSource
 from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

 ... THIS IS CONVERTING THE VIDEO FILE TO AUDIO...
 command = 'ffmpeg -i <yourvideo.mp4> -ab 160k -ar 44100 -vn <youraudio.mp3>'
 subprocess.call(command, shell=True)


 ... YOUR API DETAILS...
 apikey = '<YOUR API>'
 url = '<YOUR SERVICE URL>'

 authenticator = IAMAuthenticator(apikey)
 stt = SpeechToTextV1(authenticator=authenticator)
 stt.set_service_url(url)


 with open('audio.mp3', 'rb') as f:
     res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

 ...NEXT ROW IN JUPYTER NOTEBOOK...
 res.keys()


 ...NEXT ROW IN JUPYTER NOTEBOOK...
 len(res['results'])

 ...NEXT ROW IN JUPYTER NOTEBOOK...
 text = [result['alternatives'][0]['transcript'].rstrip()+'\n' for result in res['results']]


 ...NEXT ROW IN JUPYTER NOTEBOOK...
 text = [para[0].title() + para[1:] for para in text]

 ...NEXT ROW IN JUPYTER NOTEBOOK...
 transcript = ''.join(text)


 ...NEXT ROW IN JUPYTER NOTEBOOK...
 with open('finaltext.txt','w') as fnlwrite:
     fnlwrite.writelines(transcript)
