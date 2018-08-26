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

<div style="text-align:center"><img src ="images/design-images/side-render-1-crop.png" /></div>

<div style="text-align:center"><img src ="images/design-images/top-render-1-crop.png" /></div>

The client was happy with the general shape of this design, focusing on ergonomics as much as possible, as well as hygiene and ease of cleaning after each use. More work is required to accommodate ports, lights, and cooling. However once complete, a first print will be completed, to see how well it looks, prints and feels in the hand, and if any adjustments need to be made.

The device will be mounted into the internal cavity, and the camera into the lid, with the IR filter sitting in the large recess on top. It is unclear how this will be achieved, but we are currently looking into acquiring a small adapter that can be fastened into the recess and the lens simply screwed on to.

Small magnets will hold the lid closed while the small lip on the lid will prevent it from slipping around. the IR LEDs will also be embedded into the lid in a circular pattern around the camera filter. The type of IR LED to use has become unclear, as there are conflicting resources about what wavelength to use that best penetrate the skin to visualise the veins. IR LEDs of different wavelengths will be acquired for testing, and to empirically confirm what wavelength is best, or if a mix of different wavelengths gives the best universal result (factoring in different skin colour and conditions).

There is a concern however, wavelengths nearest to the limit of infrared spectrum will be hard to obtain in a regular form factor. These LEDs seem to come in the SMD (Surface Mounted Device) form factor, with becomes more difficult to work with when soldering into a circuit, and require specialised techniques.

These concerns will be addressed in due time. It is likely however that we will find that something slightly 'suboptimal' will prove to be enough for this project.

## Governance
The ConOps have been finalised and the client is happy with the content. The only thing that remains is to create a contract and have it signed by the relevant stakeholders.

Requirements have also been developed with the client to reach a set that was accepted by the client. While these have been accepted they are subject to revision with prototyping and further research.
