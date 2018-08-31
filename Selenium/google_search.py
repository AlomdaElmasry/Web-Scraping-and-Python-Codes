import webbrowser
import new

search_term = raw_input("Enter your search query : ")
url1 = "https://www.google.co.in/?#q=" + search_term    # Form the search url

webbrowser.open(url1, new=new)  # Open the web browser