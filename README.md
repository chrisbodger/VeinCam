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
## October 2nd
The client has recieved our second complete prototype to take and provide feedback on based on their use.
Photos of the prototype can be found in the 'images' folder, and a user instructions manual can be found in the 'docs' folder.  

### Hardware
At long last, case version 2.2 finally completed a full successful print. No changes were made to the LED configuration after testing of LEDS with differing wavelengths (840 vs 940nm) proved to not improve performance of viewing veins. The case was assembled however the mounts, charging port and button hole placement was found to be all out of place (less so than previous iterations). This will be a major focus for the final design.

Instead, firm packing foam was used to hold the components in place and align the PiJuice charging port with the charging hole cutout of the case. Makeshift buttons were made to turn the system on and off without having to open the case. The camera cable was replaced as it had been found to have been damaged during testing; a discovery made when the camera failed to load at the very last minute prior to client handover. This was replaced, tested and found to have resolved the issue.

## Software
A first attempt of a handover to the client with a makeshift prototype was made on Saturday, however the streaming web page would not load. This was found to have been due to an imcomplete line of code left in the script, due to having not saved the changes made. As a result, the main script would not complile. This was quickly resolved, but to ensure operational integrity during the client's testing, the system's operating system was wiped and reloaded with only the necessary files. This was performed to ensure there were no conflicting files that could cause issues during client use. 

Variable control using Flask via HTML is still in development, to be ready for the final version. 

## September 25th
Several weeks have gone by since the last update, and theres much to talk about:

### Hardware
We are up to case version 2.2, that incorporates a smaller form factor and better ergonomics. Unfortunately these past few weeks have not been able to produce a successful print of the new case. We believe that this will be the final iteration of the case.

The only variation to the case that may happen is testing into a different LED configuration. the aim is to attempt to achieve a better contrast of skin and veins, and hope to achieve deeper skin penetration to visualise veins on people who have a higher BMI. This is still on going but we hope to have a clear idea by the end of this week.

### Software
The software currently works to automatically start up on boot up; initialising the wireless access point for external connections and starting the web stream to an external device. It has been noted that the wireless access point fails to start sometimes, making it difficult to connect to externally. This will be looked into as it is believed that there is other software that may be interfering with the hosting software and blocking it from starting.

Aside from this, some manual controls will be implemented to the hosting web page for better control over the software processing and image input.

### Governance and Bureaucratic Issues
Over the source of the mid semester teaching break the team was in contact with a variety of sources to discuss the purpose of the device and how that impacts the how we distribute information about the device. Through much discussion, the group decided the best path for the future of the project would be to advertise the device as an educational tool, assisting with teaching about veins and educating the public for informed consent of medical procedures. 

Additionally, through correspondence with legal services and the ANU Human Ethics Committee, the group became aware that initial human testing of the device would not be able to be completed at this stage of the project as human ethics approval is necessary to do testing. This provides some roadblocks for the development of the device as the group is not able to determine how the device needs to be improved for optimal practical use. As such, the aims and scope of the project were modified slightly. 

Going forward, the group will be finishing up with tutorial documents on how to build the device, documents for conducting future testing, and acting on feedback from the client on the functioning of the device. The group is also developing designs for the poster to present the device at the closure of this project. 


## Previous Progress Updates
* [August 1st](Progress-Updates/progress-update-2018-08-01.md)
* [August 7th](Progress-Updates/progress-update-2018-08-07.md)
* [August 11th](Progress-Updates/progress-update-2018-08-11.md)
* [August 18th](Progress-Updates/progress-update-2018-08-18.md)
* [August 25th](Progress-Updates/progress-update-2018-08-25.md)
* [September 5th](Progress-Updates/progress-update-2018-09-05.md)

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
