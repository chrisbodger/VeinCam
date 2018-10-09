# Concept of Operations

Version 1.1 Signed-off by stakeholders as of 9/10/2018.

## Table of Contents
* [Project Vision](#project-vision)
  * [Value Proposition](#value-proposition)
  * [Project Scope](#project-scope)
  * [Project Comparison](#project-comparison)
* [Stakeholders](#stakeholders)
  * [Project Team](#project-team)
  * [Project Client](#project-client)
  * [Shadow Team](#shadow-team)
  * [Course Tutor](#course-tutor)
  * [Course Convenor](#course-convenor)
  * [Users](#users)
* [Resources](#resources)
  * [Funding](#funding)
  * [Tools](#tools)
* [Project Management](#project-management)
  * [Deliverables](#deliverables)
  * [Milestones](#milestones)
  * [Audit Goals](#audit-goals)
  * [Timelines](#timelines)
  * [Work Breakdown Structure](#work-breakdown-structure)
  * [Decision Making and Conflict Resolution](#decision-making-and-conflict-resolution)
* [Risk Analysis](#risk-analysis)
  * [Safety Risk Analysis](#safety-risk-analysis)
* [References](#references)
* [Change Log](#change-log)

---

## Project Vision
The VeinCam is based on the [Venenfinder project](https://hackaday.io/project/26158-assistance-system-for-vein-detection) submitted during the 2017 HackADay event. The goal was to create an affordable device that produces a clear image of a suitable vein for superficial venous puncture, a procedure that is a requirement for patient blood testing and the delivery of external drug administration. However the goal of this project is to extend the customer base to educators and students while maintaining affordability and accessibility.

### Value Proposition
Our VeinCam device will help students better understand venous sites by augmenting visualisation of upper limb veins. It will provide students with a better understanding of venous sites around the body compared to an image or model. The VeinCam is not intended for use as a medical device.
### Project Scope
The project aims to greatly extend and refine what was achieved in the Venenfinder HackADay project; automating and adding to some of the functionality while remaining cost effective.

The device should be portable and widely accessible. Veins will be illuminated using near-infrared light and the scattering from this light detected by a Raspberry Pi device equipped with a Pi noIR module. The project will be looking exclusively looking at using a Raspberry Pi as the basis for the device as has been suggested by the client due to the Pi platform being available internationally as a well established product for such uses. Additionally the Pi system has a rich set of add-on devices that support development of a vein camera.

The software from the Venenfinder project will be heavily modified, incorporating intelligent OpenCV scripts to perform automatic adjustments to the lighting and contrast settings. Manual adjustments will also be implemented in order to get the best possible image in any use case.

### Project Comparison
As this project is building on what was achieved by the Venenfinder project, it is worth noting what is being added.

#### Feature Summary
| Venenfinder | VeinCam | Future Development |
| :---: | :---: | :---: |
| IR Illumination | IR Illumination | Various Skin Conditions |
| Camera | Camera | Vein Identification |
| Manual Brightness Adjustment | Auto Brightness Adjustment | Smaller Platform |
| Manual Contrast Adjustment | Auto Contrast Adjustment | Extended Battery Life |
| Manual IR Adjustment | Auto IR Adjustment | . |
| . | Wireless | . |
| . | Portable | . |
| . | Smaller Footprint | . |
| . | AI Image Processing | . |

#### Venenfinder Features
The Venenfinder team were able to produce a device that was able to use a near-Infrared light to illuminate a patient's veins. The device uses a Raspberry Pi, a noIR camera module, and a 3x3 array of IR LEDs. Brightness of the LEDs and contrast ratios were manually adjusted using potentiometers to adjust intercepted voltages between the array and the RPi. The camera image is then streamed to a secondary web enabled device through a web browser. This method works for devices ranging from mobile phones to desktop PCs.  Unfortunately the device was quite large and bulky, resulting in the need for an external power source.

#### VeinCam Core Features
The VeinCam project hopes to utilise similar hardware to the Venenfinder project (Raspberry Pi, PiCam, IR LEDs) and extend the software's capabilities to automatically adjust the infrared light filtration, brightness and contrast to produce the clearest image possible with limited manual adjustment.

Further adding to the Venenfinder project; the aim is to produce a device that is battery powered, completely wireless and to reduce the size of the device to be comfortably held in one hand. Being a wireless device, we need to ensure the device is as power efficient as possible and does not require recharging more than absolutely necessary. As part of the new housing for the device, a mounting system will be integrated, and a mount be devised for hands-free use. 


#### VeinCam Testing and Future Development Plans
Once the core device has reached the prototype stage in-house testing will be completed on the device to determine its functionality and improve the technical aspects. The device will also be informally tested as a proof-of-concept.

Formally conducting testing requires ethics approval which is outside the scope of this project. Examining the formal testing processes will provide the project pathways to continue into the future. 
To formally verify and validate the device extensive testing will need to be completed on varying skin conditions and appearances such as: complexion, hairy, tattooed areas and other skin abnormalities (barring skin irritations such as rash and infection). The prototype will also be tested with potential users of the system to ensure that it functions acceptably; feedback will be taken to revise the prototype. Similarly potential users will be asked to construct the VeinCam so it can be ensured that the device will be independently constructible as necessary if the device is successful. 

Also requiring further investigation and implementation; the device may be able to be shrunk to a smaller platform, such as the Raspberry Pi Zero. This would allow for the device to become a lot cheaper to build, reducing the size to something that fits into the palm of your hand, and be able to conserve more power. Implementations and performance would need to be investigated, as the Pi Zero may not be able to process the video stream as effectively as its larger counterpart.

---

## Stakeholders
The following groups have been identified as stakeholders for this project:

| Stakeholder | Project Interaction |
| --- | --- |
| Project Team | Produces the Project Output and actions constructive feedback from other stakeholders |
| Project Client | Provides feedback on project progress |
| Shadow Team | Observes the Project and provides constructive feedback |
| Course Tutor | Provides feedback on project progress |
| Course Convenor | Provides feedback on project progress |

### Project Team
The project team consists of four undergraduate engineers who each have roles as point people in the project. All members of the team should be present to support each other in whatever way is necessary to complete tasks and better the project. The designated roles give each member a lead position, they are responsible for their sections and as such if any questions from external stakeholders specifically address a section of the project they are the member to contact.

| Name | Role | Email |
| --- | --- | --- |
| Christopher Bodger | Lead Hardware Engineer | u5395595@anu.edu.au |
| Alexander Ollman | Lead Programmer | u5826805@anu.edu.au |
| Stephanie Pratt | Stakeholder Liaison, Lead Researcher | u5822871@anu.edu.au |
| Jonathan McPhail | Secretary | u5351489@anu.edu.au |

#### Responsibilities of the project team to the project
* Fulfil the tasks assigned by the team within the desired time frame to the best of their ability.
* Communicate the progress and setbacks of their tasks regularly with the team.
* Commit to regularly attending scheduled meetings, or otherwise remain up to date with meeting minutes and contributing to meeting agendas.

##### Responsibilities of the Lead Hardware Engineer
* Manage and design the hardware of the device.
* Design and test the layout and chassis of the device.
* Manufacture the prototype device.

##### Responsibilities of the Lead Programmer
* Design the code for the device to meet deliverables and requirements.

##### Responsibilities of the Stakeholder Liaison
* Be the point of contact for general communication between stakeholders.
* Organise meetings with the client and other stakeholders when necessary.

##### Responsibilities of the Lead Researcher
* Perform research required to strengthen the project.
* Delegate research when necessary to other team members.

##### Responsibilities of the Secretary
* Maintain the repository and landing page.
  * Including all documentation and meeting agendas/minutes.

**To reiterate these roles show who questions should be directed to and are not indicative of workload.**

### Project Client
Ben Healey (message2ben@gmail.com)

Ben is medical student at the ANU and an employee of ACT Health. He personally began this project using pointers from open source projects such as the 2017 HackADay project and the Venenfinder project, to develop an affordable vein imaging device.

#### Responsibilities of the project team to the client
* Design a device to meet the established baseline requirements that the client has presented.
* Keep the client regularly updated with milestones and setbacks.

#### Responsibilities of the client to the project
* Provide information and requirements about the project to the team.
* Respond to communications on a regular basis.
* Be present and prepared at scheduled meetings.

### Shadow Team
ANU undergraduate engineering students, tasked with reviewing this project to provide an external viewpoint on the outputs and governance of the project.

| Name | Email |
| --- | --- |
| Ethan Stanbury | u6048363@anu.edu.au |
| Jiacong Zhao | u6029134@anu.edu.au |
| Jiarui Wang | u5879960@anu.edu.au |
| Liam Highmore | u5563628@anu.edu.au |
| Namisha Chabbra | u5644087@anu.edu.au |
| Yifei Ren | u6137095@anu.edu.au |

#### Responsibilities of the project team to the shadow team
* Provide shadows access to all information surrounding the project, including repositories, documentation and relevant communications.  This information should be up-to-date and presented appropriately.
* Be open to feedback from all channels from shadows, and act on feedback appropriately.

#### Responsibilities of the shadow team to the project
* Remain up-to-date with the activities, outputs and governance of the project through information that is supplied to them.
* Commit to providing constructive, accurate and actionable feedback to the project through the pathways provided to them: including formal audit feedback, as well as verbal feedback in tutorial sessions and through the feedback forms supplied.

### Course Tutor
Jenny Simmons (jenny.simmons@anu.edu.au)

ANU ENGN4221 course tutor for Semester 2 2018. Tasked with formally organising and directing weekly tutorial sessions where the project is planned, presented and reflected upon.

#### Responsibilities of the project team to the course tutor
* Provide the tutor access to all information surrounding the project, including repositories, documentation and relevant communications. This information should be up-to-date and presented appropriately.
* Be open to feedback from the tutor, and act on feedback from all channels appropriately.
* Be present and prepared at all weekly tutorials (Tuesday 10-12), appropriate to the activity of the tutorial that week.
* Be informed of the structure of the course and related assessment milestones as established by the course convenor.
* Be prepared to submit assessments, and be open to grades and discussion of grades with the course tutor.

#### Responsibilities of the course tutor to the project
* Be present and prepared to lead the tutorial each week, appropriate to the activity of the tutorial, and remain up-to-date with the progress of the project.
* To a reasonable extent, assist the project team with the progress of the project, including answering relevant and reasonable questions, and providing constructive, actionable and accurate feedback, particularly at times of project audits and during tutorial sessions.
* Reply to correspondence (email) in a timely fashion, and grade formal assignments fairly and appropriate to the quality of the project.

### Course Convenor
Chris Browne (chris.browne@anu.edu.au)

ANU ENGN4221 course convenor for Semester 2 2018. The course convenor is the overall authority and organiser for this course, and hence the projects that run through this course.

#### Responsibilities of the project team to the course convenor
* Same as those applying to the course tutor.

#### Responsibilities of the course convenor to the project
* Same as the course tutor with the addition of:
* Organise the course appropriate to the desired outcomes and be receptive to feedback regarding this structure. Information regarding the structure and assessment milestones of the course should be available to students within a reasonable timeframe.

### Users
Members of the public, particularly students and educators who wish to utilse the device for educational purposes. 

#### Responsibilities of the project team to the users
* Provide members of the public access to information that pertains to all aspects of the project.
* Design a device that, at minimum, must not endanger the safety of potential users.
* To the best of their ability, provide the public with the information to design an affordable device that can image the veins of a person.

#### Responsibilities of the users to the project
* Members of the public have little steadfast responsibility to the project team.
* Ideally, members of the public will provide feedback on the function of the device during requirements analysis or testing.

---

## Resources
### Funding
At most, the project should cost no more than the $400 proposed in the design brief. This will include the hardware and components necessary.

Ideally, the project should cost less than this. A [Bill of Materials](#bill-of-materials) with associated can be seen below. This is likely to be updated as the prototype is developed and costs are encountered. All additional proposed costs will be agreed upon by key stakeholders before purchase.

### Tools

Tools likely to be used throughout this project include:
- Soldering Iron
- 3D Printer
- Laser Cutter
- Dremel
- Screwdriver, screws, nuts and bolts.

All safety precautions outlined by the ANU Makerspace's Terms and Conditions will be followed during the use of instrument or tool, regardless of where and how it is used. A safety risk analysis has been performed at the bottom of this document.

#### Project Administration
* GitHub
* GitHub Pages
* Google Drive
* Facebook Messenger Platform

#### Manufacturing and Testing
* Ian Ross Design Studio
* ANU Makerspace

##### Bill of Materials
An initial Bill of Materials has been drafted below of what we expect the project to cost.

| Component | Cost (AUD) | Supplied By Client |
| --- | :---: | :---: |
| Raspberry Pi 3 | $65 | Y |
| Raspberry PiCam | $50 | Y |
| Raspberry Pi Battery Module | $90 | Y |
| 10 x 840nm near-Infrared LEDs | $22 | N |
| 10 x 220 Ohm Resistors | $5 | N |
| 8 x Disk Neodymium Magnets | $5 | N |
| 3 x Cuboid Neodymium Magnets | $4.50 | N |
| IR Filter | $10 | Y |
| 1kg Filament | $34 | N |
| Total | $240 |   |

Please note these pricings are indicative and can change with the market. It is also worth noting that the client was kind enough to provide most of the hardware, as we can see in the table. This means the required costs during our development will be minimal to purchase the remaining inexpensive components.

#### Programming
* Source code from the Venenfinder HackADay project has been utilised, as it achieves close to the client's desired deliverable. This code will then be modified to achieve the client's desired features, including auto-vein focus.

---

## Project Management
### Deliverables
The initial deliverables are as follows:  

#### Baseline Deliverables
* Configure device based on Venenfinder to be able to automatically adjust contrast.
* Design and manufacture a prototype chassis to house Pi modules to allow for handsfree, real-time visualization.
* Produce a "how to build" and "how to use" guides for the device.
* Perform initial in-house testing on the device itself (not formal user-testing).

#### Stretch Deliverables
In order of priority.
* Implement manual controls for image adjustment.
* Compile user feedback on the construction and use of the device (based on the written guides).
* Optimise for different use-case scenarios (e.g. tattooed skin, dark skin).
* Design or source an appropriate hands free stand to mount the device.
* Optimise device to visualise blood flow to identify best candidate vein

#### Ultra-Stretch Deliverables or Future Project Aims
* Configure device to run off of Pi Zero module
  * Offload image processing to secondary device

### Milestones
Further detail on the optimisation of milestones and design aims of the prototype are detailed in the Requirements document.

#### Milestone 1
Construct functional prototype based off of Venenfinder design.

#### Milestone 2
Configure software to automate brightness and contrast of vein visualisation, and design hardware to reduce product's form factor.

#### Milestone 3
Initial AutoCAD design of 3D-printable chassis, maximize automatic focus and brightness to optimise software enhancement of the captured raw image for clear image definition.

#### Milestone 4
Final AutoCAD design and phyiscal print-out of chassis, accompanying web/smartphone appication to display camera image, contain adjustable settings, and optimise battery life and charging scenario.

### Audit Goals
#### Audit 1
* Complete ConOps Version 1

#### Audit 2
* Update ConOps to Version 2
* Complete requirements analysis
* Reach Milestone 2

#### Audit 3
* Achieve Milestone 3/4 with accompanying verification and validation

Milestones are subject to change as the project evolves.

### Timelines
An [indicative schedule](https://docs.google.com/spreadsheets/d/1nfNqFCF2ieP5CyVmqDSeZ3oXegxcCG4hojdd6fMcq9Y/edit?usp=sharing) has been drafted for the project.

### Work Breakdown Structure
1. Requirements Analysis  
   1.1. Review PoC  
   1.2. Perform risk analysis  
   1.3. Brainstorm requirements (in-house)  
   1.4. Develop requirements with client  
   1.5. Finalise requirements  
2. Prototyping  
   2.1. Design hardware  
   2.2. Manufacture and construct hardware  
   2.3. Design baseline software  
   2.4. Integrate software  
   2.5. Update software with stretch deliverables
3. Validation & Verification  
   3.1. Test prototype in-house  
   3.2. Conduct performance review  
4. Documentation  
   4.1. Write ConOps v1  
   4.2. Update ConOps v2  
   4.3. Create "How-to" guide  
   4.4. Create poster  
   4.5. Organise repository  

### Decision Making and Conflict Resolution
Decision making will be by consensus in consultation with the client. When consensus cannot be reached the project team will seek advice from other stakeholders depending on the nature of the decision. For further detail please refer to the [Decision Log](/docs/Decision-Log.md).

---

## Risk Analysis
All risk analysis performed throughout this project will be in accordance to the Australian and New Zealand Industry Standard AS/NZS 4360:2004.

![Risk Matrix](https://github.com/chrisbodger/VeinCam/blob/master/images/ConOps/risk-matrix.png)

Potential risks to the success of the project have been brainstormed in order to understand them and mitigate either their severity or likelihood.

| Risk | Consequences | Likelihood | Severity | Mitigation |
| :---: | :---: | :---: | :---: | :---: |
| Not clearly understanding or defining client's requirements for the project. | Product does not meet client requirements, client dissatisfied, requires re-doing work, going over budget and schedule to redesign | D | 3 | Maintain regular contact with client regarding progress and milestone completion. |
| Not defining scope of project and setting clear and achievable milestones. | No clear definition of project progress, feature creep over time results in lack of physical product, no clear "stopping point" for project or completed product, client dissatisifed, product does not meet customer requirements, likely to be over-budget. | C | 3 | Defining scope early and ensuring we stick to milestones and their respective outputs to ensure we do not deviate on a project tangent. |
| Device cannot be utilized as a medical device due to not meeting medical certification criteria. | Unable to deliver product to medical professionals, which is client's ultimate goal for the project. | C | 2 | Ensure client is aware of potential certification issues, and that they verify during development whether the device can be used with and/or without the medical classification. |

### Safety Risk Analysis
In developing the prototype there is a chance of injury, similar to above these risks have been listed and steps taken to mitigate their severity or likelihood.

| Risk | Consequences | Likelihood | Severity | Mitigation |
| :---: | :---: | :---: | :---: | :---: |
| Personal harm whilst using listed tools (incl. burns, shocks, cuts) | Pain, discomfort and possible medical attention. | D | 3 | Ensuring all team members are familiar with the safety training of the ANU Makerspace/Engineering workshop, supervision by one other team member when using potentially dangerous tools. |
| Damage to Hardware due to physical impact or electrostatic discharge (ESD) | Loss of data, hardware faliure, schedule delays to order and replace damaged hardware. | E | 4 | Ensuring hardware is never placed in an area where it is likely to be damaged, always in full visible sight. Observing proper ESD safety techniques, such as regularly grounding ourselves and only contacting circuitry by edges. |

---

## References
[Venenfinder Github](https://github.com/Myrijam/Venenfinder)

[Venenfinder HackAThon Page](https://hackaday.io/project/26158-assistance-system-for-vein-detection)

---

## Change Log

| Version | Section | Change | Justification |
| --- | --- | --- | --- |
| 1.1 | [Project Vision](#project-vision) | Adjust project vision to create an educational device. | There are a lot of responsibilities for a medical device manufacturer. Developing the VeinCam for an educational purpose removes these responsibilities. |
| 1.1 | [Project Management](#project-management) | Added how-to build and how-to use guides, and device testing to baseline deliverables. | Missing from previous deliverables and necessary for open-source construction and verification. |
| 1.1 | [Project Management](#project-management) | Added manual adjustment and user feedback deliverables. | Considered more important than the other stretch deliverables as it will enhance the user experience and is more achievable. Testing will provide points for the project to move forward. |
| 1.1 | [WBS](#work-breakdown-structure) | Removed testing with users. | No longer falls within the scope of the project and would require ethics approval. |
| 1.1 | Value proposition, VeinCam testing, Users and Baseline deliverables | Formally stated not intended as a medical device. Making it clear testing is only in-house and any further testing is detailed only for future development of the project. Adjustment of users to specify students and educators as per the revised purpose of the device. | As per changes recommended by the client to align with re-purposing of the device for educational purposes. |

This Project is licensed under the Creative Commons license.
