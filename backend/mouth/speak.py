import pygame
import random
import asyncio
import edge_tts
import os

allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 :,.?!"

def remove_special_chars(text):
    newtxt=""
    for i in text:
        if i in allow:
            newtxt+=i
    return newtxt

def fnsample(r=None):
    return True

async def amain(text) -> None:
    """Main function"""
    file_path = r"Backend\data.mp3"

    if os.path.exists(file_path):
        os.remove(file_path)
    communicate = edge_tts.Communicate(text, 'hi-IN-MadhurNeural',pitch='+5Hz', rate='+22%')
    await communicate.save(r'Backend\data.mp3')

def TextToSpeech(Text):

      def Speak(*args,fn=fnsample,**kwargs):
            r=[str(i) for i in args]
            data=" ".join(r)
            data=remove_special_chars(data)
            while 1:
                  try:
                        asyncio.run(amain(data))
                        pygame.mixer.init()
                        pygame.mixer.music.load(r"Backend\data.mp3")
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy():
                              if fn()==False:
                                    break
                              pygame.time.Clock().tick(10)
                        return 
                        
                  except Exception as e:
                        pass

                  finally:
                        fn(False)
                        pygame.mixer.init()
                        pygame.mixer.music.stop()
                        pygame.mixer.quit()

      Data = str(Text).split(".")
      responses = [
      "The text has been successfully printed on the chat screen, awaiting for your review.",
      "Your requested text has been printed on the chat screen for your convenience, sir.",
      "Sir, the printed text is now visible on the chat screen, please take a look.",
      "The text has been rendered on the chat screen as per your instruction, sir.",
      "You'll find the text printed on the chat screen, ready for your inspection, sir.",
      "The chat screen now displays the printed text, sir, awaiting your feedback.",
      "The printed text is now visible on the chat screen for your perusal, sir.",
      "Sir, the text has been successfully printed on the chat screen for your review.",
      "The chat screen now showcases the printed text, sir, please have a look.",
      "You'll find the result displayed on the chat screen, sir, ready for your assessment."
      ]

      if len(Data)>8:
            if len(Text)>=350:
                  Speak(random.choice(responses))

            else:
                  Speak(Text)

      else:
            Speak(Text)

TextToSpeech("hi")