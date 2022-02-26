import requests
import webbrowser

def showCatImage(url): 
    response = requests.get(url)
    responseURL = str(response.json()[0]["url"])
    webbrowser.open(responseURL)

def showShibaImage(url):
    response = requests.get(url)
    responseURL = str(response.json()[0])
    webbrowser.open(responseURL)


def questionOnStart():
    goodResponses = {"Good", "good", "GOOD"}
    badResponses = {"Bad", "BAD", "bad"}
    hungryRespones = {"Hungry", "hungry", "Hungry"}
    quitResponses = {"QUIT", "quit", "Quit"}
    validResponses = set.union(goodResponses, badResponses, hungryRespones, quitResponses)

    answer = input("Hi! How are you feeling? ('Good/Bad/Hungry') (or... quit)\n(Enter your response) ")

    if(answer not in validResponses):
        print("Sorry but you must enter a valid response ;-; !!!")
        answer = input("Hi! How are you feeling? ('Good/Bad/Hungry') (or... quit)\n(Enter your response): ")
    elif (answer in goodResponses):
        print("I'm so happy for you!!! Keep up the hard work here is a cute cat picture for your hard work :D")
        showCatImage("https://api.thecatapi.com/v1/images/search")
    elif (answer in badResponses):
        answer2 = input("Awww I'm sorry to hear ;-; do you want cute cat or shina-inu pictures ;-;\n(Only enter 'cat' for cat picture or 'shiba' for shiba-inu picture) " )
        if(answer2 == "cat"):
            showCatImage("https://api.thecatapi.com/v1/images/search")
        elif(answer2 == "shiba"):
            showShibaImage("http://shibe.online/api/shibes?")
    elif(answer in quitResponses):
        print("Bye-bye!")
        quit()


questionOnStart()
