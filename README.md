# The Plan

Hello,

Unfortunately, due to a mistake, I am unable to finish this project. I attempted to run both React and Django's REST framework in one repository, but somehow missed that I needed to do a good amount of set-up work at the very beginning to make that work, including several specifically placed installs I have not done. It doesn't help that the documentation guiding me on how to do that was only released 3 days ago as of writing this, and given that, to guareenteably complete this so that it definitely functions, I'll need to start over entirely, then even with the ability to copy a good amount of this work over to a new repo for the Project, it will still take at least a couple of days just to make sure all the connections between the two actually work.

As such, I'm leaving this document to show what I had intended, which I will hopefully be in a position to actually do come the resubmission, though I know that will restrict me to a Pass. At the very least, I completed most/all of the backend, with the only parts I feel still needed completing being adding a Completion boolean to the Tasks Model and a small issue of the user being able to assign other users' Tasks to their Groups.

First, I intended for the app to open up to an introductory screen that would be visible to all users not yet logged in or registered. It would welcome the user to the program, and explain what it was for: to allow the user to set Tasks with due dates so as to keep track of them, and to allow them to set Groups connected to those Tasks containing info on the people who would be working on them. Directly beneath this would be the options to log in or register.

After doing so, the nav bar would appear, allowing the user to open their Profile if they wished to edit it, as well as to move between Tasks and Groups. By default, the Tasks data would be shown, taking the form of a table containing the title, due date, and completion status of every Task the user had created, as well as the options to View, Edit, or Delete them, all in order of their due dates from earliest to latest. They would also be able to add new Tasks

The user would then be able to change the order of display for their tasks, as well as to Search them for specific titles. Upon pressing View, the user's display would change to an expanded view of that specific task, showing the title and due date, but also the description, which the user would naturally be able to add to their Task on creation or edit. The Edit and Delete buttons would do what you'd expect.

Selecting Groups would change the display to show the user a table of their Groups, if they have any. This table would show the assigned task and number of people in the Group, as well as the View Edit and Delete options. The expanded version View would show, much like for the Tasks, would allow the user to see the description of the group, which contains all details the user thought relevant in relation to the Group. It's kept freeform to allow the user to freely decide what form this takes, from a simple list of member names, to potentially even a record of who is meant to do what and when, all within a text field.

Obviously, the user would also be able to make new Groups.

That covers pretty much all the important plans.

# NOTE:

I used the Moments template for this project