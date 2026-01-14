# Todo: Importing beautiful soup verison 4
from bs4 import BeautifulSoup



# Todo:  Opening and collecting the data from the html file;
with open("./website.html") as file:
     contents = file.read()


# Todo: Using the beautuful soup module
                # notes class( MARKUP(I.E. the code for the html), parser( what language?))
soup = BeautifulSoup(contents,"html.parser" )
                        # In some cases you may need to use lmxl parser. Parser is just a way to read the website
                        # The soup acts as an object hat can tap into any part of the html code. Therefore, allowing you
                        ## to tap into the html object using python code.

#---------------------------------------Functionalities----------------------------------------------------------------#
            # All of these functionalities that only capture the first instance of it
# Entire tag
print(soup.title)

# Tag function
print(soup.title.name)

# Tag string
print(soup.title.string)

# Can use prettify to place the indentations
print(soup.prettify())

# Can also get the first anchor tag/ li/p:
print(soup.li)

# Can use the function ---->find_all( name = tag name)
all_anchor_tags = soup.find_all(name = "a")

    # Can also capture the text within the anchor tag using:
for tag in all_anchor_tags:
    print( tag.getText)
    pass

for tag in all_anchor_tags:
    # Need to isolate the link within the tag
    tag.get("href")

# Can also search using the identifiers to find the tag of the identifier( class and tags)
heading = soup.find(name= "h1" , id="name")
            #soup.find is only applicable for a first instance of an event
            #same thing applied to clas function. Class is a reserve function. Onely can be used to create classes.
            # Therefore, need an underscore when you cal it
section_heading = soup.find(name= "h3", class_ ="heading")

#------------------------------------The use of the css selector-------------------------------------------------------#
company_url= soup.select_one(selector="p a")
## in the css code this should come out as p a {................}

# Can use the # class aa the selector within the css code.
    # can also do it by class
soup.select(selector =".heading" )