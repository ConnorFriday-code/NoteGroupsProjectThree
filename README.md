![Logo of Note Groups!]()
# Note Groups!

## UX

### Project Goal
The goal of 'Note Groups!' is to create a website that hosts documents created by the user. The website will be broken into three template webpages: Home, Note, and Create Note. Home will display all created notes as postit notes, which when clicked on will take the user to that note. The note will be displayed on the Note page, and will be filled in with data from the database. Lastily, the link Create Note will lead the user to a page where they name and create a new note, which will automatically load the new note on creation.

#### Minimum viable product goals

The minumum viable product would have the home page list all Notes with no specified ordering and no styling, displaying the title the user gives the document. These Notes when clicked on will open a page containing text saved to the document id in the database. The Create Note link will successfully create a new note that will store content into the database and appear on the homepage.

#### Additional goals

Additional features I wish for the website are to be user complimentary features. A search bar at the top of the homepage to search through existing Notes, and when no results are found, instead offer a link to the Create Note page. Inside the Note page, the user will have the ability to add basic text effects to the documents, such as bold, italic and crossed-out text, as well as change font size, font colour, and font background/highlight, with these css stylings being saved to the database as well. The list of notes on the Homepage to be ordered by the last saved document. Add a way for the user to add multiple notes/text documents to a Note (to make a 'Note Group').

### User goals

#### First Time User

- To be able to quickly and easily navigate the layout of the website
- To be able to create a new note in three clicks or less
- To be able to create a note and save it to the database

#### Returning User

- To be able to load already created notes
- To be able to edit old notes and have those changes replace the old document
- To be able to delete a note in four clicks while still having protective measures

#### Dedicated User

- To be able to search through multiple notes on the homapage with ease by making notes titles clear, easy to read, and possibly with a search bar
- For notes to load quickly even at larger sizes
- For the homepage to load notes at an acceptable speed

### Design

#### Colour Choices

I wish to mimic the appearence of paper notes, like the lined paper in a note book or a shopping list, and as such I have decided to go for a white background, light grey accents/borders, and pale/soft colours. Then further borrowing the aesthetics from sticky notes, I came to the decision that my colours could be green, yellow, blue, or pink, the most common and famous colours of sticky notes, and ultimately decided I will go with a pale yellow.

I decided to choose yellow due to two reasons:

1. Colour theory explains the colour yellow is assossiated with happyness, with pleasent positive emotions
2. The same yellow can be used as for the high-lighter if I can add the additional goal of css styling being saved to the database, create a constant colour pallete across the webpage

With my choices of white, grey, and pale yellow chosen, I have decided to dedicate these colours to:

##### White
- The background of all pages
- The background of the notes
- The background of buttons
- The background of the header
- The text colour of buttons on click/mousedown
- Footer text colour

##### Grey
- Borders on divs
- The border of buttons
- The background of buttons on click/mousedown
- Border of notes on the homepage

##### Yellow
- The background of flash messages
- The background of the footer
- The background of buttons in navigation

Text will remain generic black unless specified elsewhere.

#### Wireframes and logic

#### Wireframe

![Image of all wireframes and colours used](readme_folder/wireframe_and_database/wireframes_project_3.png)

#### Databse Logic

Down below is the planned database columns and their data storage types.

|Data column|Data type
|:---|:---|
|id|Int
|title|Str
|description|Str
|note_content|Txt
|date_updated|Date

'id' Will be the primary key and will increment with every new note created/enters the entry.
<br>
'title' Will be a string to be displayed on the home page and at the top of a note.
<br>
'description' Is an optional field and will be displayed on the home page.
<br>
'note_content' Will be the content of the note. I plan to save it as an html with user being able to 'edit' the html with a rich text editor.
<br>
'date_updated' Will contain the date whenever the file is updated for sorting on the homepage.

## Final Features/Product

### Deployment

#### GitHub
#### Heroku And The Database

#### Creating the database

The first step was installing Flask, SQLAlchemy, and psycop using the following command line in the terminal:

pip3 install 'Flask-SQLAlchemy<3' psycopg2 sqlalchemy==1.4.46

Afterwards, I had to update Flask to a later model due to avoid hitting an error later, as advice by a college in one of meetings with our tutor. The command line used in the terminal was as follows:

pip3 install --upgrade --user Flask==2.3.3

With the sytems in place, I quickly built the initial required pages for a website (such as run.py, home.html etc.) before creating models.py. This is to contain the database schema for all the notes. This is what the created code looks like below:

![Img of models.py code](<readme_folder/creating_database/new database_1.png>)

Afterwards, I proceded to update my routes.py to import 'Notes' from the above module for future use.

![Img of routes.py updated with Notes import](<readme_folder/creating_database/new database_2.png>)

I followed this up by then connecting to sql and creating the databse in the terminal.

![Creating database in postgresql in the terminal](<readme_folder/creating_database/new database_3.png>)

I then used the python interpetor in the terminal to make the postgres database populated with the table from models.py.

![Python in terminal to add table to the database](<readme_folder/creating_database/new database_4.png>)

### Features

#### 404 Page

### Erros solving
#### Bug fixing
#### Validators

## Technology Used

### Code
### Media/Content
### Thanks And Acknowledgements
