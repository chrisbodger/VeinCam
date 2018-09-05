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