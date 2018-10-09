# ENGN4221 VeinCam Project Team Work Diary

Instruction: Team members to add progress of assigned tasks, including date of update and team member/s involved.


## Hardware and Software Activities

Progress from start of project as at 15/08/2018
* Assembled the hardware into the proposed configuration
* Installed and prepared the operating system as per the VeinCam Tutorial (Install OS, OpenCV and PaspAP softwares).
* Performed testing of the hardware with sample code provided by the Raspberry Pi documentation.

17/08/2018
* Alex researching into the implementation of manual software controls in a HTML web page space - intermediary step to automatic controls. Rudimentary control methods in place, yet to make them actionable.
* Chris designing an enclosure for the device and components using CAD software. Several concepts in mind, looking for a compact, ergonomic form factor.

18/08/2018
* Preliminary design of the case presented to the client. He was overall happy with the design as it stands. will continue to work on to add further features to accommodate the Pi device.

22/08/2018
* The first prototype (v1.0) case design ready to be printed. Chris will start the print in the makerspace overnight and will need to picked up the following day.

23/08/2018

**Hardware**
* Case v1.0 printed successfully, with a few minor defects. The simple supports for the Pi were easy to break, and most of the support material did not come away easily. Case v1.1 should be started today, hopefully to be picked up tomorrow for ANU Open Day. V1.1 brings stronger Pi supports, a more flush interface with the lid, enlarged openings for the IR LEDs, and a 180 degree reorientation when printing. this reorientation will generate more support material, but will hopefulle make for an easier clean up post print.
* The case shell was cleaned as best as possible and was determined to be too large for small hands. v2.0 has begun to address this, cutting the size down by almost 10mm all round. a proper mounting solution for the LED array will be embedded into the case lid as well, when the LED array has been constructed and finalised. further design improvementments to be implemented after our weekly meeting with the client.

**Software**
* Scrapping the manual controls for the moment. Focussed more on the image processing and getting a clear, defined image of veins for Open Day. Constructed an script using OpenCV which would capture an image, perform a histogram equalisation of the image, and then feed the equalised image into a stream. The next major goal will be to parse this video stream into a web page that can be accessed by any external device.

27/08/2018

**Hardware**
* Alex constructed the LED array to be placed in the newly 3D-printed v1.1 enclosure for a full demonstration of our first complete prototype during the Audit 2 presentation.

**Presentation**
* Steph presented our project to the tutors and tutorial group, including our shadow team. We received great feedback and plenty of questions, which gave us an idea of how others external to the group viewed our progress. The topics of commercialisation and hygiene (sterilizing our product for hospital environments) were raised and gave the group plenty to think about when considering the final design. The prototype demonstration went very well.

30/08/2018

**Hardware**
* Version 2.0 of the chassis has been completed, and printed has started on it for completion and assessment over the coming days. further changes are expected, and hopefully they will be minor so that it can be handed over to the client for testing, pending completion of the software.

03/09/2018 - 04/09/2018

**Software**
* Solved issue of sending processed images to stream by scrapping old streaming code and instead using Flask (based on code by Miguel Grinberg at https://blog.miguelgrinberg.com/post/video-streaming-with-flask). Device can now stream live images to WLAN localhost at 60fps, meaning any device can connect to the network outputted by the RasPi and view the stream.
* After many hours, we also managed to get the streaming script to run on startup. This ensures that all a user has to do is press the power button and the device will begin streaming (after 30 second boot time) to its localhost address.
* Cleaned up HTML code, which now displays correct fonts and current RasPi temperature (for testing purposes).
* Currently working on displaying Battery percentage on stream web page and improving the image processing capabilities.


06/09/2018 Joey
* v2.1 of the chassis, including buttons and both shell and lid started (speed set to 50mm/s to ensure clean print)

18/09/2018 Chris
Retrospective Recount of the last two weeks:
* Attempted several times to print case v2.1, with no success. Attempts would either fail to print entirely, or would not print cleanly, and leaving features malformed.
* Due to so much wastage from the failed prints, a new roll of filament was ordered 7/9/18. The replacement roll arrived 14/9/18.
* v2.2 of the chassis was created, altering the shape to take on more of an hourglass, in an effort to make the case easier to hold by the ends. Currently, this revision is being printed, and seems to be printing well. smaller features yet to be printed to see if this remains the same.

* Software completed the autostart and initialisation procedures for the web stream and image processing. Currently, it outputs the processed image at a reasonably high framerate for its intended use. The webpage however has an issue initialising the stream in a timely manner (upwards of 30 seconds) and the Wireless connectivity fails to initiate on some occurrences. These will hopefully be explored in the coming weeks.

25/09/2018 Chris
Started work on an alternative LED array to try and achieve deep vein visualisation. An array of both 850nm and 940nm has been laid out but yet to be tested. The case lid has been slightly altered to be able to house 12 LEDs in preparation of success.

Printing the case has been continually failed since last term, regardless of the printer and variation of settings. We will need to speak to one of the technicians on how to successfully print the case.

29/09/2018 Chris, Alex
After the failure of the device during handover to the client. the Software Team agreed that it would be best to rebuild the operating system, as the behaviours presented (failure to broadcast a visible wifi, failure to initiate the camera web stream) could not be pinpointed to any one thing. Despite the time consumption to prepare the operating system, it would have taken even more time to fix these errors.

The operating system was prepared in full by end of day.

01/10/2018 Chris, Alex
The script runs consistently and reliably, along with the wifi connectivity. we initially had issues starting the script as it was worked into the system profile and the profile was not being sourced, thus the camera script not starting. The system was told to boot into its Command Line Interface, and switched back to GUI mode before we noticed the script running on start up. as of that evening, after multiple reboots and shut downs, the device continued to work as intended, and is ready for handover on 02/10/2018. A backup of the system was taken in case something were to go wrong.

## Documentation, Research, Meetings and other Governance Activities

Progress from start of project as at 15/8/18
* First draft of ConOps Complete not yet signed off from stakeholders
* First draft of Requirements complete, awaiting feedback from Client
* Work breakdown structure and corresponding Gantt Chart constructed
* 7 meetings so far, all minutes available on repository, 4 group meetings (every Wednesday 11am) and 3 client meetings (Saturdays 2pm weekly as needed)
* Landing page draft complete
* First Project Audit complete (7/8/18), feedback received and action tasks assigned accordingly
* Steph and Joey currently assigned research
* Decision log created and first contribution added

15/8/18 Steph, Alex, Joey
* Group meeting conducted. Minutes recorded.

15/8/18 Steph
* Feedback from client for conops reviewed and ConOps updated accordingly
* feedback from client for requirements received

16/8/18 Steph, Joey
* Issues added, Joey to address client feedback requirements
  * Feedback addressed, awaiting confirmation at client meeting.

16/8/18 Joey
* Decision Making/Conflict Resolution added to ConOps and Decision Log.
  * Column "Stakeholders Involved" added to decision log.

20/8/18 Joey
* Landing page changed over to a more public friendly style

21/8/18 Steph
* Reviewed email from Client regarding sourcing LEDs - pass this on to the team
* Received confirmation from Convenor regarding Open Day presenting
* Requested Client permission for Open Day presenting

22/8/18 Steph
* Reviewed email from Client confirming permission for Open Day presenting
* Created resources file in the Git to store info about purchasing new hardware
* Emailed Convenor about Open Day
* Client passed on that he has linked veincam.org to the Github site

22/8/18 Joey
* Font-style of landing page adjuest to client's original type.
* ConOps contract created.
* Initial market research performed, at least four competitors found.
* Landing page content updated.
* Work diary link added to readme.
* Added small section in testing to the ConOps.

7/9/18 Steph
*  Purchase log created

24/8/18 Steph
* Sent microgrant application to Course convenor
* Completed research regarding medical device classification, regulation and marketing. Will upload this onto Git in the next week
* Basic draft of audit 2 presentation started

25/8/18 ALL project team
* Open day presentation and user testing
* Signoff of Conops and requirements by team and client

27/8/18 Steph
* Sent conops agreement to project tutor for signoff - received signoff. Updated ConOps for Version 1.0 with all stakeholders signoff
* Received acceptance of microgrant ($40) from course convenor.

27/8/18 Joey
* Updated the public landing page with a few new images and current state of the project.

27/8/18 Alex and Chris
* Discussion regarding next phase of hardware and software development, including defining and finalising modifications to the v2.0 design of the enclosure.

28/8/18 Steph
* Created user feedback document in resources file of repository
* Updated user feedback with preliminary results from open day 25/8/18
* Created research document, starting compiling research

4/9/18 Joey
* Created initial site design and architecture,
* Created site pages to expand the website. Not yet complete.

11/9/18 Steph
* Meeting with ANUSA Lawyer to discuss liability issues
* Email sent to TGA regarding medical device definition and compliance
* Research done on human ethics

12/9/18 Steph
* Email sent to technology transfer office to make booking
* Email sent to ANU human ethics committee regarding need to ethics approval
* Appointment made with ANU Technology Transfer Office

14/9/18 Joey
* Initial testing documents created.

17/9/18 Steph
* Brief meeting with course convenor with project update
* Emailed client about project updates and forwarded correspondence from ethics committee
* Emailed other course lecturer about medical devices
* Made agenda for tutorial tomorrow 18/9
* Begun agenda for group meeting 19/9
* Written up audit 2 feedback summary, lawyer meeting summary and human ethics committee summary of correspondence

24/9/18
* Brief meeting with course convenor on biomedical materials  to discuss purpose of the device
* No new information for project

25/9/18 Joey
* Reworked sections of the ConOps (as seen in change log in rebranding patch).

26/9/18 Joey
* Began changes to requirements document with rebranding.

29/9/18 Joey
* Completed changes to requirements and testing documents.

1/10/18 Joey
* ConOps v1.1 pdf created based on version in patch.

8/10/18 Steph
* Client feedback document created in resources
* Conops v1.1 updates as per client feedback (see change log)
* Created Audit 3 presentation and poster survey
* First draft of Handover document
* Microgrant 2.0
