from gtts import gTTS
import os

te_xt="Tum Itna Jo Muskura Rahe Ho  Kya Gham Hai Jisko Chhupa Rahe Ho  tum itna jo muskura rahe ho  Ankho Mei Nami Hasi Labo Par  Kya Haal Hai Kya Dikha Rahe Ho  kya gam hai jisko chhupa rahe ho tum itna kyo muskura rahe ho  Ban Jayenge Zehar Peete Peete  Yeh Ashk Jo Pite Ja Rahe Ho Jin Zakhmo Ko Waqt Bhar Chala Hai Tum Kyo Unhe Chhedhe Ja Rahe Ho kya gam hai jisko chhupa rahe ho tum itna kyo muskura rahe ho"

language = 'en'

output = gTTS(text=te_xt, lang=language, slow=False)

output.save("Text-To-Speech.mp3")

os.system("start Text-To-Speech.mp3")