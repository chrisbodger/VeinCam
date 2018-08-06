# Concept of Operations

## Table of Contents
* [Project Vision](#project-vision)
  * [Value Proposition](#value-proposition)
  * [Project Scope](#project-scope)
* [Stakeholders](#stakeholders)
  * [Project Team](#project-team)
* [Resources](#resources)
  * [Funding](#funding)
  * [Tools](#tools)
  * [Project Administration](#project-administration)
  * [Manufacturing and Testing](#manufacturing-and-testing)
    * [Bill of Materials](#bill-of-materials)
  * [Programming](#programming)
* [Project Management](#project-management)
  * [Milestones](#milestones)
  * [Deliverables](#deliverables)
    * [Audit 1](#audit-1)
    * [Audit 2](#audit-2)
    * [Audit 3](#audit-2)
  * [Poster and Presentation](#poster-andpresentation)
  * [Timelines](#timelines)
  * [Work Breakdown Structure](#work-breakdown-structure)
* [Deliverables](#deliverables)
* [Risk Analysis](#risks-analysis)
* [Safety Risk Analysis](#safety-risk-analysis)
* [References](#references)

---

## Project Vision
The VeinCam is based on the [Venenfinder project](https://hackaday.io/project/26158-assistance-system-for-vein-detection) submitted during the 2017 HackADay event. The goal was to create an affordable device that produces a clear image of a suitable vein for superficial venous puncture, a procedure that is a requirement for patient blood testing and the delivery of external drug administration.

### Value Proposition
Our VeinCam device will help medical professionals who want to perform intravenous procedures by externally visualising a patient’s veins. It will increase the likelihood of successfully accessing those veins to reduce patient discomfort and increase medical staff efficiency.

### Project Scope
The project aims to build on what was achieved in the Venenfinder project; automating and adding to some of the functions while remaining a cost effective solution. Ideally, the device will be able to be built and used by patients with chronic diseases that regularly require personal drug administration.

The device should be portable, hands-free and wireless. Veins will be illuminated using near-infrared light, and the scattering from this light detected by a Raspberry Pi device equipped with a PiCam module.

Due to the variation in human skin in its absorption of different wavelengths of light, an unclear image can be produced, a proper candidate may be undetected. Having an auto-switch feature to automatically adjust the wavelength emitted will build on what has already been achieved. This adjusts the contrast of the image to allow for the easier detection of veins, with minimal to no input from the user.

---

## Stakeholders
The following groups have been identified as stakeholders for this project:
* Project Client - Provides feedback on project progress
* Project Team - Produces the Project Output and actions constructive feedback from other stakeholders
* Shadow Team - Observes the Project and provides constructive feedback
* Course Tutor - Provides feedback on project progress
* Course Convener - Provides feedback on project progress

### Project Team
The project team consists of four undergraduate engineers:

| Name | Role |
| --- | --- |
| Christopher Bodger | Lead Mechanical Engineer |
| Alexander Ollman | Lead Programmer |
| Stephanie Pratt | Stakeholder Liaison |
| Jonathan McPhail | Secretary |

Ben Healey is our client for this project, currently an ANU Medical Student, and employee of ACT Health.

---

## Resources
### Funding
At most, the project should cost no more than the $400 proposed in the design brief. This will include the hardware and components necessary.

Ideally, the project should cost less than this. A [Bill of Materials](#bill-of-materials) with associated can be seen below.

### Tools
Several Tools will be used for this project, and they are listed below

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

| Component | Cost | Supplied By Client |
| --- | :---: | :---: |
| Raspberry Pi 3 |   | Y |
| Raspberry PiCam |   | Y |
| Raspberry Pi Battery Module |   | Y |
| 940nm near-Infrared LEDs |   | N |
| 220 Ohm Resistors |   | N |
| Rotary Encoders |   | N |
| 40 Pin Female Header |   | N |
| Neodymium Magnets |   | N |
| IR Filter |   | N |
| Total |   |   |


#### Programming
* Source code from the Venenfinder HackADay project has been utilised, as it achieves close to the client's desired deliverable. This code will then be modified to achieve the client's desired features, including auto-vein focus.

---

## Project Management
### Deliverables
The initial deliverables are as follows:  

#### Baseline Deliverable
* Configure device based on Venenfinder to be able to adjust contrast.

#### Stretch Deliverables
* Design and manufacture a prototype chassis to house Pi modules to allow for handsfree real time visualization
* Configure device to run off of Pi Zero module
* Optimise for different use-case scenarios (e.g. tattooed skin, dark skin)
* Optimise device to visualise blood flow to identify best candidate vein

### Milestones
#### Milestone 1
Construct Functional prototype based off of Venenfinder design.

#### Milestone 2
Configure software to auto-focus and design hardware to reduce product's form factor.

#### Milestone 3
Initial AutoCAD design of 3D-printable chassis, maximize auto-focus function for clear image definition.

#### Milestone 4
Final AutoCAD design and phyiscal print-out of chassis, accompanying web/smartphone appication to display camera image, contain adjustable settings.

### Audit Goals
#### Audit 1
* Complete ConOps Version 1

#### Audit 2
* Update ConOps to Version 2
* Complete requirements analysis
* Reach Milestone 2

#### Audit 3
* Reach Milestone 4 with accompanying verification and validation

Milestones are subject to change as the project evolves.

### Timelines
An indicative schedule has been drafted for the project.

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
   3.1. Test prototyype in-house  
   3.2. Test prototype with users  
   3.3. Conduct performance review  
4. Documentation  
   4.1. Write ConOps v1  
   4.2. Update ConOps v2  
   4.3. Create poster  
   4.4. Organise repository  

---

## Risk Analysis
At this initial project stage, the risks involved with this project lie within the governance of the project itself. Risks associated with the product and its physical development will be stated in ConOps prior to Audit 2.

An initial Project Risk Assessment can be seen below.

| Risk | Consequences | Likelihood | Severity |
| :---: | :---: | :---: | :---: |
| Not clearly understanding or defining client's requirements for the project. | Product does not meet client requirements, client disatisfied, requires redoing work, going over budget and schedule to redesign |  |  |
| Not defining scope of project and setting clear and achieveable milestones. | No clear definition of project progress, feature creep over time results in lack of physical product, no clear "stopping point" for project or completed product, client disatisifed, product does not meet customer requirements, likely to be overbudget. |  |  |

### Safety Risk Analysis
To be completed prior to the commencement of the project construction, as well as Audit 2.

---

## References
[Venenfinder Github](https://github.com/Myrijam/Venenfinder)

[Venenfinder HackAThon Page](https://hackaday.io/project/26158-assistance-system-for-vein-detection)


This Project is licensed under the Creative Commons license.
