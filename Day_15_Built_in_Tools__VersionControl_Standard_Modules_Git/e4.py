import webbrowser

user_term = input("Enter a Search term: ").replace(" ", "+")

webbrowser.open("https://google.com/search?q=" + user_term)

