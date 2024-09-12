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

I decided to choose yellow due to three reasons:

1. Colour theory explains the colour yellow is assossiated with happyness, with pleasent positive emotions
2. The same yellow can be used as for the high-lighter if I can add the additional goal of css styling being saved to the database, create a constant colour pallete across the webpage
3. It matches the colour of standard paper notes

I decided to choose white due to two reasons:
1. The colour white has high contrast range, especially with black which is standard
2. The brightness/high value keeps the website feeling light and enegetic

I decided to choose light grey due to two reasons:
1. It works as a good border/accent colour to both yellow and white
2. It matches the colour of the lines usually found in notes and note pads
3. Not an aggressive colour, it will not tear the user's attention away from the content of the website by being distracting

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

By comparing my notes of listed features, both 'minimum viable product goals' and 'additional goals', from the start of the README, I can test if I have achieved them.

#### Current Features

#### Features to be added

### User goals

### Languages Used

### Frameworks, Libraries & Programs Used

### Error solving

#### Bug fixing

#### Submit error

I had noticed while using Quill's api that you can insert an 'a'/href link in the text area. However, when the user uses this feature, they click on a 'save' button to create the link. The note seems to work fine until the user tries to save the note itself later. Saving the note break it for ever by making the note uneditable html afterwards, regardless if the user closes and reopens the note. This also happens with bold text and and the bullet list option.

Before:

![Before save is clicked](readme_folder/bug-fixing/link-bug-1.png)

Afterwards:

![After save is clicked](readme_folder/bug-fixing/link-bug-2.png)

Seeing as the edits/additions to the notes are being successfully submitted to the databse, this seems to be a rendering error and not a submission error. This is further proven with a syntex error on the line of code that edits the text area's html to be filled with the saved html content (quill.root.innerHTML = "{{ note.note_content|safe }}";) (image below).

![Code](readme_folder/bug-fixing/link-bug-5.png)

Looking into the console for an explanation gave two errors:

Syntax error

No resource found with given identifier

![Error in console](readme_folder/bug-fixing/link-bug-4.png)

I promptly search for these errors involving Quill, yet do not find any results related to my problem. The reason for this I believe is that quill uses its own method to save its data using the methods getContent and setContent. Yet, even when implmenting these two methods into my code, I still encountered errors. After 8 hours, I still could not get the text editor to accept any special characters or CSS styling in the text editor area.

This led to me having to make the choice: rewriting the website, database, routes, and javascript files, or, cutting out the CSS/special characters features.

Due to time restraint of the project, I decided to cut the features instead of trying to fix an api I did not understand. Thus bug fixing now became trying to find a way to remove the features currently breaking the editor.

Searching the api documents I find the section that discussed the toolbar and options. The link to it is <a href="https://quilljs.com/docs/modules/toolbar" target="_blank">here</a>

There it lists code to be put into the script section of a html page to dictate what options will be available to the user, and using this, cut down the available selection down to: headers, bold, italic, and underline.

![Code list](readme_folder/bug-fixing/link-bug-6.png)

I have tested that the remaining options do not break the editor.

![Updated code](readme_folder/bug-fixing/link-bug-7.png)

Now, regardless if I use any of the remaining options in any combonation, the editor will save and display without breaking.

![Test editor with all options](readme_folder/bug-fixing/link-bug-8.png)

## Testing

### BBD vs TDD

#### Differences between BDD and TDD

The main difference between BDD (Behaviour Driven Development) and TDD (Test Driven Development) is that BDD is about tests being done manually while TDD is about tests being checked automatically by the computer. TDD is written before the software and improved to meet updated goals, the cycle repeating over and over until the product is finished and passes all tests. BDD is tested as the code is written against the user stories, with the user manually checking changes on different media and screen sizes until completion. BDD tests can cause the program to end up feeling more intuitive and require no software, leading it to be simpler for a developer. Meanwhile, TDD can test extreme conditions and more conditions at a very fast rate, causing the program to end up being more stable.

#### Why I chose BDD testing

#### BDD example with group notes

When I, the user, enter the website, I wish:
* To be able to navigate the navigation bar with ease
* To be able to edit the my notes
* To have all links work

### Testing user goals using BDD

Using the user goals I listed at the start of the README, I can use BDD testing to check if I have achieved the goals:

#### First-time users

#### Returning user

#### Dedicated user

### Validators

## Technology Used

### Code/Media/Content

<a href="https://validator.w3.org/">W3C</a>

Used to find errors and help correct them in my HTML.

<a href="https://jigsaw.w3.org/css-validator/">Jigsaw</a>

Used to find errors and help correct them in my CSS.

<a href="https://jshint.com/">jshint</a>

Used to find errors and help correct them in my JS.

<a href="https://fonts.google.com/">Google Fonts</a>

Used in title elements using the Ubuntu family of fonts.

### Thanks And Acknowledgements

Code Institute for teaching me the knowledge of web development and providing a library of resources to return to for help.
