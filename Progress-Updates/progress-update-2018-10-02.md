## October 2nd
The client has recieved our second complete prototype to take and provide feedback on based on their use.
Photos of the prototype can be found in the 'images' folder, and a user instructions manual above in the main respository.  

### Hardware
At long last, case version 2.2 finally completed a full successful print. No changes were made to the LED configuration after testing of LEDS with differing wavelengths (840 vs 940nm) proved to not improve performance of viewing veins. The case was assembled however the mounts, charging port and button hole placement was found to be all out of place (less so than previous iterations). This will be a major focus for the final design.

Instead, firm packing foam was used to hold the components in place and align the PiJuice charging port with the charging hole cutout of the case. Makeshift buttons were made to turn the system on and off without having to open the case. The camera cable was replaced as it had been found to have been damaged during testing; a discovery made when the camera failed to load at the very last minute prior to client handover. This was replaced, tested and found to have resolved the issue.

### Software
A first attempt of a handover to the client with a makeshift prototype was made on Saturday, however the streaming web page would not load. This was found to have been due to an imcomplete line of code left in the script, due to having not saved the changes made. As a result, the main script would not complile. This was quickly resolved, but to ensure operational integrity during the client's testing, the system's operating system was wiped and reloaded with only the necessary files. This was performed to ensure there were no conflicting files that could cause issues during client use.

Variable control using Flask via HTML is still in development, to be ready for the final version. 
