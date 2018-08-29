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
## August 25th
### Hardware/Software
We have had a productive week on the hardware and software side of the project. We have successfully printed a prototype of the chassis, and have begun iterating on it to make it more suitable for the final product. A second print with some minor adjustments is underway and should be completed by our audit tutorial.

We found that the first chassis that was printed was quite large to hold, even by those with larger hands, and certainly would pose a challenge to hold by people with smaller hands. We determined that there was a lot of wasted space inside where the device is stored, and the next version will remove a lot of this space to slim down the device. The second version is currently being drawn up which will correct the dimensions and include a proper mounting system for the LED array, and after we have a time to inspect the v1.1 changes, more will be discovered and corrected in v2.0 and beyond. A new LED array will be constructed to be embedded in the new chassis.

On the side of software, we were able to achieve a histogram equalisation of a single frames, and push those frames to a local high frame-per-second video stream. This is a huge step towards our next milestone, and a step closer to finalising our product. The next goal for the project software is to feed the equalized video stream into the web stream so it can displayed on an external device, as well as applying colour filtering to further enhance the definition of veins.

### ANU Open Day
The VeinCam team volunteered to showcase the project to visitors, including many ANU student prospects, during this year's ANU Open Day. Throughout the day, we aimed to try and gauge public interest and acceptance, as well as user testing and receiving specific feedback. It was great opportunity to have a large number of people of diverse skin types test our product to determine where we can improve the product at such an early stage so we can gauge what adjustments need to be made.

We tested the device on many different skin colours, and noticed the skin tone appeared to not be an issue in displaying a prominent image of the veins, with both lighter skin tones and a range of darker skin tones tested.  A substantial amount of arm hair was thought to be an issue with vein detection, but this was proved not to be the case, as the small sample of testers with a significant portion of arm hair had their veins show up quite clearly. 

We had a small number of people with skin conditions visit, including eczema, calloused skin and blemishes. Unfortunately, the device was not able to detect veins underneath sections where calloused skin was present, which we thought it due to the areas being to thick for the IR light to penetrate. The other skin conditions were no issue in regards to vein detection. There were no tests on those with tattoos on the day.

Vein detection through varying degrees of body fat was a primary concern of our client. Some testers came through with larger amounts of body fat around their arms, or simply had veins that were not on the surface of the skin, in which they were not able to have their veins detected by the device. The ability to detect veins through varying degrees of tissue will be very important function to focus on, as it may potentially determine whether or not our product can be used by a majority population and thus meet our project goals.

It was also observed that lots of external lighting, most prominently fluorescent lights and sunlight, produce enough infrared (IR) light to affect our project's ability to clearly deifne veins. The histogram equalisation software was not able to adjust the contrast of the stream as there was too much ambient IR light in the room, and skewed the histogram of the image itself to be more in the whiter zones, and washing out the darker zones. We are still looking into ways of resolving this, but one method may be purchasing an IR filter for the device for a longer wavelength (~800nm) so more light is filtered out, and hopefully making the overall image darker. A software solution may exist which we will also be exploring.

Overall, our project received a lot of interest and patrons were intrigued and impressed with what we presented on the day; validating our progress and urging us to continue moving forward. 
 
### Other Admin/Governance 
Regarding documentation updates, we have now received signoff from all stakeholders for our Concept of Operations. Research is well underway to get a good idea of the product market, as well as information on commercialisation and medical procedures around the VeinCam. 

## Previous Progress Updates
* [August 1st](Progress-Updates/progress-update-2018-08-01.md)
* [August 7th](Progress-Updates/progress-update-2018-08-07.md)
* [August 11th](Progress-Updates/progress-update-2018-08-11.md)
* [August 18th](Progress-Updates/progress-update-2018-08-18.md)

## Work Diary
For more detailed information on the work that has been completed please refer to the [work diary](docs/Team-Work-Diary.md)

# 3. Audit Log
Here we will have the information, results, and feedback to our audits, and will be presented in the following links (as they are created):

* Audit 1
* Audit 2
* Audit 3

Should our stakeholders wish to provide us with feedback, they can fill out a google survey in which we will action them appropriately as responses are presented to us.

# 4. Concept of Operations
Our Concept of Operations is nearly complete. after we have completed the feedback from Audit 1, we feel that this document will be ready for sign off.

The [Concept of Operations](docs/CONOPS.md) document can be found in our repository.

# 5. Meeting Minutes
Team meetings are scheduled twice a week, to ensure the team is aware of the overall progress made, as well to provide the client an opportunity to see what we have achieved, should they choose to join the meetings. They are currently scheduled for the following times:
* Wednesday 11pm
* Saturday 2pm

The Saturday Meeting is primarily made available for meeting with the client, and to provide a weekly update, where Wednesday is an internal midweek meeting to ensure our actionables are on track for completion. These times may vary, depending on the availability of the team, and client.

Meeting Minutes can also be found in our repository:

## Last Meeting Minutes
* [August 28th](Meeting-Minutes/Meeting-Minutes-2018-08-28.md)

## Previous Meeting Minutes
* [July 31st](Meeting-Minutes/Meeting-Minutes-2018-07-31.md)  
* [August 1st](Meeting-Minutes/Meeting-Minutes-2018-08-01.md)
* [August 4th](Meeting-Minutes/Meeting-Minutes-2018-08-04.md)
* [August 8th](Meeting-Minutes/Meeting-Minutes-2018-08-08.md)
* [August 11th](Meeting-Minutes/Meeting-Minutes-2018-08-11.md)
* [August 14th](Meeting-Minutes/Meeting-Minutes-2018-08-14.md)
* [August 15th](Meeting-Minutes/Meeting-Minutes-2018-08-15.md)
* [August 18th](Meeting-Minutes/Meeting-Minutes-2018-08-18.md)
* [August 22nd](Meeting-Minutes/Meeting-Minutes-2018-08-22.md)
* [August 25th](Meeting-Minutes/Meeting-Minutes-2018-08-25.md)

# 6. Design Documents
The design of the VeinCam will be presented here, once the ConOps has been approved, and progress/final designs are made available. the construction method of the device will also be presented here.
