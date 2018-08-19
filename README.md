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
## August 18th
It has been a light week this week in terms of progress. We focused on finalising our documentation with the client.

### Hardware/Software Update
#### Software
**Software** has hit a wall for the first time during this project. After the successive progress of preliminary testing of different programs in relation of what features were to be added to the project, it was the attempted merging of them that has slowed us down.

Python has a built-in HTML layer, which allows us to produce a stream from the camera and present it onto a web page for viewing on any web-enabled device. HTML natively has very little support for the execution of python scripts, which is essentially what the hardware runs on. This week has been research week, attempting to look into various programming languages as well as more complex extensions of Python to bridge the gap between HTML and Python. small progress has been made, as the creation of manual controls can be seen in the same window as the video stream. these controls are not functional at the time of writing, as the bridge between the two languages is still missing.

It was also decided that the permanence of these manual controls is ideal, for 2 reasons:
1. it allows the developers to absolutely understand how the adjustments to the image stream can be achieved for when the automatic controls are implemented
2. it provides a backup in case the automatic adjust is not able to produce a clear image, and intervention is required.

This week will include further research onto how to overcome this obstacle, and move forward into successfully implementing these controls. We hope to have this obstacle cleared by the next audit.

#### Hardware
**Hardware** have begun a preliminary design for the outward appearance of the device, which we can see below.

**EDIT IMAGES TO FIT PROPERLY**

The client was happy with the general shape of this design, focusing on ergonomics as much as possible, as well as hygiene and ease of cleaning after each use. More work is required to accommodate ports, lights, and cooling. However once complete, a first print will be completed, to see how well it looks, prints and feels in the hand, and if any adjustments need to be made.

The device will be mounted into the internal cavity, and the camera into the lid, with the IR filter sitting in the large recess on top. It is unclear how this will be achieved, but we are currently looking into acquiring a small adapter that can be fastened into the recess and the lens simply screwed on to.

Small magnets will hold the lid closed while the small lip on the lid will prevent it from slipping around. the IR LEDs will also be embedded into the lid in a circular pattern around the camera filter. The type of IR LED to use has become unclear, as there are conflicting resources about what wavelength to use that best penetrate the skin to visualise the veins. IR LEDs of different wavelengths will be acquired for testing, and to empirically confirm what wavelength is best, or if a mix of different wavelengths gives the best universal result (factoring in different skin colour and conditions).

There is a concern however, wavelengths nearest to the limit of infrared spectrum will be hard to obtain in a regular form factor. These LEDs seem to come in the SMD (Surface Mounted Device) form factor, with becomes more difficult to work with when soldering into a circuit, and require specialised techniques.

These concerns will be addressed in due time. It is likely however that we will find that something slightly 'suboptimal' will prove to be enough for this project.

## Governance
The ConOps have been finalised and the client is happy with the content. The only thing that remains is to create a contract and have it signed by the relevant stakeholders.

Requirements have also been developed with the client to reach a set that was accepted by the client. While these have been accepted they are subject to revision with prototyping and further research.

### Research (Steph to add?)


## Previous Progress Updates
* [August 1st](Progress-Updates/progress-update-2018-08-01.md)
* [August 7th](Progress-Updates/progress-update-2018-08-07.md)
* [August 11th](Progress-Updates/progress-update-2018-08-11.md)

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
* [August 15th](Meeting-Minutes/Meeting-Minutes-2018-08-15.md)

## Previous Meeting Minutes
* [July 31st](Meeting-Minutes/Meeting-Minutes-2018-07-31.md)  
* [August 1st](Meeting-Minutes/Meeting-Minutes-2018-08-01.md)
* [August 4th](Meeting-Minutes/Meeting-Minutes-2018-08-04.md)
* [August 8th](Meeting-Minutes/Meeting-Minutes-2018-08-08.md)
* [August 11th](Meeting-Minutes/Meeting-Minutes-2018-08-11.md)
* [August 14th](Meeting-Minutes/Meeting-Minutes-2018-08-14.md)

# 6. Design Documents
The design of the VeinCam will be presented here, once the ConOps has been approved, and progress/final designs are made available. the construction method of the device will also be presented here.
