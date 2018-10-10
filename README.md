# Table Of Contents
1. [Feedback](#1-feedback)
2. [Progress Update](#2-progress-update)
3. [Audit Log](#3-audit-log)
4. [Concept of Operations](#4-concept-of-operations)
5. [Meeting Minutes](#5-meeting-minutes)
6. [Design Documents](#6-design-documents)

# 1. Feedback
A feedback form has been created for the interest of our stakeholders, should they wish to pass on any changes or improvements they believe to be prudent. The form can be found [here](https://goo.gl/forms/8cw5eWdaOY5C1jBo1).

Once the feedback has been received, an issue will be created within the GitHub repository for public viewing and tracking.  
**Any feedback is welcome.**

# 2. Progress Update
## October 9th

### Software

Implimented buttons into the HTML video streaming page, which trigger Flask/Python functions to set the camera parameters of brightness, contrast and saturation for the next frame. These buttons were designed to be large and use appropriate colours (red for lower, green for higher) in order to be intuative and intended for an educational audience. Following a meeting with the client after the testing, the stream is now shown in portrait rather than landscape to take advantage of the fact most users will be streaming to their personal devices in a portrait orientation, as well as being able to view someone's arm verticaly along the webpage.

All code had been uploaded into the software folder, including a complete image file which can be written to an SD card and used immediately with a Raspberry Pi and a PiCam (a method which has been tested and validated!). If the user does not have a PiJuice shield, minor adjustments must be made to app.py (see README.md in software folder or /home/pi/pistream in image for details).

#### A chronological work diary of software development throughout this project has also been added to the software folder.

### Audit 3 Presentation

The VeinCam was presented at our final Audit presentation during our tutorial timeslot. The final version was demonstrated to shadows and tutor. A draft of the poster to be presented next week was shown for feedback. The feedback given on the physical design, product functionality and overall presentation was very positive.

## Previous Progress Updates
* [August 1st](Progress-Updates/progress-update-2018-08-01.md)
* [August 7th](Progress-Updates/progress-update-2018-08-07.md)
* [August 11th](Progress-Updates/progress-update-2018-08-11.md)
* [August 18th](Progress-Updates/progress-update-2018-08-18.md)
* [August 25th](Progress-Updates/progress-update-2018-08-25.md)
* [September 5th](Progress-Updates/progress-update-2018-09-05.md)
* [September 25th](Progress-Updates/progress-update-2018-09-25.md)
* [October 2nd](Progress-Updates/progress-update-2018-10-02.md)

## Work Diary
For more detailed information on the work that has been completed please refer to the [work diary](docs/Team-Work-Diary.md)

# 3. Audit Log
Here we will have the information, results, and feedback to our audits, and will be presented in the following links (as they are created):

* Audit 1
* Audit 2
* Audit 3

Should our stakeholders wish to provide us with feedback, they can fill out a google survey in which we will action them appropriately as responses are presented to us.

# 4. Concept of Operations
Our Concept of Operations has undergone further iterations in recent weeks, primarily to the aims, scope and stakeholders of the project. We encourage any feedback on changes made.

The [Concept of Operations](docs/CONOPS.md) document can be found in our repository.

# 5. Meeting Minutes
Team meetings are scheduled two to three times a week with different stakeholders present. One meeting is internal with only the project team, one has the tutor and shadow team present, and one is with the project client. They are currently scheduled for the following times:
* Tuesday 10am (Tutor and Shadow Team)
* Wednesday 11pm (Project Team)
* Saturday 2pm (Project Client)

The wednesday and saturday meeting times may vary, depending on the availability of the team, and client.

Meeting Minutes can also be found in our repository:

## Last Meeting Minutes
* [September 29th](Meeting-Minutes/Meeting-Minutes-2018-09-29.md)

## Recent Meeting Minutes
* [September 5th](Meeting-Minutes/Meeting-Minutes-2018-09-05.md)  
* [September 15th](Meeting-Minutes/Meeting-Minutes-2018-09-15.md)
* [September 18th](Meeting-Minutes/Meeting-Minutes-2018-09-18.md)
* [September 19th](Meeting-Minutes/Meeting-Minutes-2018-09-19.md)
* [September 22nd](Meeting-Minutes/Meeting-Minutes-2018-09-22.md)

# 6. Design Documents
The design of the VeinCam will be presented here, once the ConOps has been approved, and progress/final designs are made available. the construction method of the device will also be presented here.
