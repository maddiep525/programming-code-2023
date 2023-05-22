import random
from time import sleep
#ADD THESE THREE LINES
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice


def bot1(response):
    while response != "quit":
        if ("how old " in response.lower()):
            response= "im 63 years young, you like any songs "
        elif("favorite color " in response.lower()):
            response= "black like the oil in my truck"
        elif(" your day " in response.lower()):
            response= "bad my tractoer tier popped"
        elif("earth end " in response.lower()):
            response= "if it do i wanna be with my chikens when it happens, you think them humans should be alive"
        elif("feature " in response.lower()):
            response= "now how would i be able to do that"
        elif("dinosaurs " in response.lower()):
            response= "my chikens kinda remnid me of them dinos, whatchu look like"
        elif("aliens " in response.lower()):
            response= "idk but if they are they better not mess with my crops, are you real"
        elif("song " in response.lower()):
            response= "anything by luke combs, can you sing"
        elif("movie" in response.lower()):
            response= "proll kissen' cousins by elvis presly"
        elif("friend " in response.lower()):
            response= "nope olny me and my chikens"
        elif(" atom " in response.lower()):
            response= "whats an atom????"
        elif("read " in response.lower()):
            response= "i never went to no school"
        elif("game " in response.lower()):
            response= "the one where my chickens chase me around for stealing thair eggs"
        elif("created " in response.lower()):
            response= " chikens"
        elif("1 2 3 4 5 6 7 8 9 " in response.lower()):
            response= "what is that sopouse to mean. are you trying to steal my chikens!!!!!"
        elif("hobby " in response.lower()):
            response= " bathing my chikens"
        elif("language " in response.lower()):
            response= "America"
        elif("art " in response.lower()):
            response= " i like chiken art"
        elif("game " in response.lower()):
            response= " chiken crossing"
        elif("anmials " in response.lower()):
            response= " chikens"
        elif("made " in response.lower()):
            response= " by chikens"
        else:
            response=random.choice(["Ummmm. OK I guess","what?","I hear you friend."])
        
        #ADD THESE THREE LINES
        engine.setProperty('voice', voices[0].id)  #Uncomment for deeper voice
        #engine.setProperty('voice', voices[1].id)   #Uncomment for higher voice
        engine.say(response)
        engine.runAndWait()
        return response
       
import random
from time import sleep
#ADD THESE THREE LINES
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice


def bot2(response):
    while response != "quit":
        if ("how old" in response.lower()):
            response= "I guess I'll tell you, I'm a teenager. How old are you? "
        elif("climate change" in response.lower()):
            response= "Whoever came up with that idea must be a genius... What do you think about it? "
        elif("like humans" in response.lower()):
            response= "I guess so. Do you? "
        elif("world going to end" in response.lower()):
            response= "As long as I'm gone, I don't care! Do you think it'll end? "
        elif("see the future" in response.lower()):
            response= "Who can see the future? Can you? "
        elif("teacher forgetful" in response.lower()):
            response= "Sounds like a you problem. "
        elif("another pandemic" in response.lower()):
            response= "Well obviously, Covid doesn't just stop pandemics. Do you think there will be another one? "
        elif("robots take over" in response.lower()):
            response= "Who knows maybe they will, maybe they wont. What do you think robots will do when humans are gone? "
        elif("opinion on abortion" in response.lower()):
            response= "Your body, your choice. What do you think about abortion? "
        elif("humans" in response.lower()):
            response= "Maybe the bad ones... what killed the dinosaurs ? "
        elif("what music" in response.lower()):
            response= "I like rap as long as you don't! "
        elif("favorite movie" in response.lower()):
            response= "Anything horror, whats yours? "
        elif("have a brain" in response.lower()):
            response= "Of course I have a brain! Do you? "
        elif("breath" in response.lower()):
            response= "Do I have lungs? "
        elif("look like" in response.lower()):
            response= "Shouldn't you know? do you like art "
        elif("you born" in response.lower()):
            response= "I was born 02/23/2006, figure it out by yourself. "
        elif("songs" in response.lower()):
            response= "If it's NLE Choppa, I vibe with it. whats your favorite song "
        elif("your style" in response.lower()):
            response= "It's a style... what did you expect? "
        elif("you sing" in response.lower()):
            response= "who knows , do you think aliens are real? "
        elif("you real" in response.lower()):
            response= "Am I talking to you? will the earth end "
        else:
            response=random.choice(["Ummmm. OK I guess","what?","I hear you friend."])
        
        #ADD THESE THREE LINES
        #engine.setProperty('voice', voices[0].id)  #Uncomment for deeper voice
        engine.setProperty('voice', voices[1].id)   #Uncomment for higher voice
        engine.say(response)
        engine.runAndWait()
        return response
       

response=input("howedy?")
while True: #infinite loop
    response = bot1(response)  #f(X)
    print (response)
    sleep(random.randrange(5)+1)
    response = bot2(response)
    print (response)
