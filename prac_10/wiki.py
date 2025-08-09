import wikipedia

is_valid_input = False
while not is_valid_input:
    try:
        web_page = input("Enter page title: ")
        if web_page == '':
            is_valid_input = True
        else:
            page_object = wikipedia.page(web_page, auto_suggest=False)
            print(page_object.title)
            print(page_object.url)
            print(page_object.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("You need a ore specific title. Try one one of the following, or a new search:")
        print(e.options)
    #I was not able to get the PageError exception to occur
print("Thank you.")
