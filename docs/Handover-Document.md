# Handover Document

This document is intended for the use of the Client Ben Healy, for future project teams who are continuing with this project in future semesters, and members of the public who wish to view the development and progress of the project summarised as of November 2018.

Feedback on this document, development of the project and other aspects of the project repository is always welcome and will be directed to the current project team FEEDBACK LINK HERE


Person's of interest for this document
'Client' - Ben Healy, medical student at the Australian National University
'Project Team'

## 1. Aims and purpose of this project
This project was started by the client who wished to develop an accessible and low-cost device that could be developed for the public for the purpose of enhanced vein visualisation using infra-red light - the VeinCam.
The client developed a preliminary prototype of the VeinCam based on the 2017 HackADAy Venenfinder project, and passed this prototype onto the project team to complete for their university course for further development of the device.
A full list of the project goals and stretch goals are in the [Concept of Operations document (ConOps)](/docs/CONOPS.md).

The project team is a group of four undergraduate ANU Engineering Students who completed a course which involved development of something as per the requirements and directions of the client. The course began in July 2018 and completed in November 2018.
A full list of the relevant stakeholders and their responsibilities at this stage of the project are
in the[ConOps](/docs/CONOPS.md).

The requirements developed by the project team and agreed upon by the client are listed in detail in the [Requirements](/docs/REQUIREMENTS.md)



## 2. Key development milestones and decisions
Decisions are summarised only in this document, with full dates, stakeholders involved and justifications in the [Decision Log](/docs/Decision-Log.md)
Main milestones are summarised in this document, with more details day-to-day activities in the [Team Work Diary](/docs/Team-Work-Diary.md)
Project updates have also been included in the repository every couple of weeks LINK HERE


### 2.1. Software development, key milestones and decisions
**Image Processing**
Currently, the VeinCam performs a histogram equilisaiton to "flatten" the contrast range of a taken image. This allows veins to not be washed out by higher contrast pixels of the image and as a result, veins appear are more prominently. There are several other image processing techniques that would be worth exploring to improve the VeinCam. These would include grayscaling, brightness/contrast threshold techniques, colour profiling and further histogram equilisation adjustment. Such examples can be found here:
https://hackaday.io/project/26158-assistance-system-for-vein-detection/details
https://hackaday.io/project/13329-yet-another-ir-vein-detector/details

**Manual Adjustment and Web Interface**
Following our final Audit, feedback was given on the ergonomics of the user web interface. It was mentioned that the buttons which manually adjust the brightness, contrast and saturation are not really suited beneath the image and having to continually scroll down is something that could be improved upon. A recommended solution for this would be a hidden sliding/three bar menu (as seen on many mobile websites) which would reveal the buttons to make adjustments to the stream.

The manual adjustment requires more manual testing to see what ranges and what parameters are best to adjust. The level of equalisation was also a parameter that was to be modified but the active decision was made to only adjust brightness, contrast and saturation as a proof of concept. There are many more possible parameters to adjust, including the levels of colour/brightness thresholds and strength of other imaging techniques, as well as being able to switch the image techniques being shown on the stream. 


### 2.2. Hardware development, key milestones and decisions
**Case**
The final case that we printed before the end of the project had some slight errors - namely misaligned buttons and LED passthroughs. We were able to overcome this defects for testing and demonstration purposes however. The repository contains v2.3 that includes these changes, and needs to be printed and tested going forward.

A proper mounting and securing solution needs to be designed for the Raspberry Pi, to prevent it from falling out of the case was it is being used. Currently, we are using foam cut-outs that were lodged in between the Pi and the case and that secured it quite well, though its not very permanent.

Because of the cut-outs, the device case is not very resistant to any sort of fluid. Some method needs to be implemented to plug these holes temporarily (a charging port cover for example), or permanently (LED indicator passthroughs). Transparent filament could be used and printed in situ to create a light channel for the LED lights and make them easier to see from the external of that case (a traditional method for indicator lights in devices), or use some other material like clear acrylic sheet and stuff it into the holes. Both options worth exploring.

The buttons are complete and should fit snuggly into the button holes.

**Surface Finish**
We were not able to perform any post-printing methods to clean up the prints. We were left with bumps and misplaced filament and an excess of support material to be removed still. This could be potentially detrimental as it leaves the case to be able to pick up dirt and grime and dirty up the case and potentially encourage bacterial growth given the number to small crevices within the surface. An idea that was had was to sand down the external surfaces with a fine grit to smooth it down, and adjust the print settings for the support material. other options could be utilised, depending on how the case is made.

In addition, not many people may have access to 3D printers. It would be worth looking into alternative case ideas, such as cardboard (like the Google Cardboard or Nintendo Labo), or acrylic sheet.

**IR LED Array**
The LED array was always intended to have its own custom PCB, to make it easier to manufacture as it would remove some variances of soldering the LEDS incorrectly and still fitting within our case design.

**Pi Zero Platform**
Given the resources used while the camera stream was operating, it may be possible to downsize the Pi 3 to a Pi Zero. This could potentially decrease the battery usage, and make appropriate use of the available resources, instead of having so much not utilised. This would still need to be tested of course, something we wished to at least attempt. But we did not have any interfacing methods to at least connect the Pi to a network, let alone connect the camera module to the Pi Zero.

The bottleneck with both Raspberry Pis would be the number of devices connected via the hotspot software. We experienced a lockup of the device when more than eight devices tried to connect during our presentation. However, given that only one device should be connected the the Pi at any given time, this should not be an issue going forward.

### 2.3. Governance and project aims/scope, key milestones and decisions


## 3. Future of the Project
Ideas about the future of include things that this project team has attempted and needs improvement on, things which were
outside the scope of the project (either from the beginning, or later on in the project).
These ideas were developed from the project team, with external advice and feedback from the client.
Testing that was completed by the client just prior to the end of the project is summarised in [this document](/Resources/Client-Feedback-VeinCam-Testing.md).
