A platform where students can access class notes shared by the lectures
And also past papers/ CAT papers

## Run Website
To run this website
1. clone the repository to your local machine.
```#!/bin/bash
git clone <url>
```
2. install requirements
```#!/bin/bash
pip install -r requirements.txt
```
3. run the app
```#!/bin/bash
flask run
```
OR

4. Debugger turned on
```#!/bin/bash
flask --app app.py --debug run 
Run with Debugger enabled
```

## REQUIREMENTS SPECIFICATION

### Technical Requirements
You can use your phone or laptop to view the website

 To view on your phone you need ot use a private or trusted network
 Then on your terminal type (Confirm your IP Address first by running ipconfig on CMD):
    ```#!/bin/bash
    flask run --host=0.0.0.0 
    ```
    Can run on your default host


### Non-functional requirements
- Data should be secure.
- The system should be light weight for ease of access and should load within two seconds.
- Should be responsive to different screen sizes.


###ISSUES
1. Lacks a download progress bar

2. Accordion does't turn dark despite dark mode settings