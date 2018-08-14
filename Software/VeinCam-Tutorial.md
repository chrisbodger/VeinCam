# Preparing a Raspberry Pi for VeinCam
Install the Raspbian operating system. At time of writing, Stretch is the latest version, and can be downloaded from the Raspeberry Pi Website. You can install either the full desktop version, or the lite version for those who are familiar with navigating through a Command Line Interface.

## Installing OpenCV
### Preparing the Filesystem
This install guide follows what is detailed [on this page](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/).
First expand the file system to fill the entire SD Card. In the terminal:
Type
```
sudo raspi-config
```

Navigate to **7. Advanced Options > A1 Expand Filesystem** and step through any prompts. Reboot the Pi if prompted to do so after expanding the filesystem, otherwise type the following into the terminal.
```
sudo reboot
```

Once rebooted, the file system should fill the SD card. You can use ```df -h``` to check this. ```/dev/root``` should be a similar size to the SD Card.

**IMAGE**

Some space can be freed from the default install by removing some software. Wolfram and Libreoffice will not be used on the platform, and takes up around a 1GB of storage. Use the code below to remove these applications from the system:
```
sudo apt-get purge wolfram-engine
sudo apt-get purge libreoffice*
sudo apt-get clean
sudo apt-get autoremove
```
the purge commands will remove the core applications, while the clean and autoremove clear out any links to the applications, and remove any unused dependencies for more free space. this may take several minutes to complete.


### Installing the OpenCV Dependencies
Especially if you are starting from a fresh install of Raspbian, it is crucial to update the system, to ensure the repository and core system functions are up to date.
```
sudo apt-get update && sudo apt-get upgrade
```
This command will update the repository first, then update the system using the now updated repository. again, this may take several minutes to complete - depending on your Pi and internet connection.

Next is to install the compiling packages
```
sudo apt-get install build-essential cmake pkg-config
```

the next commands install various packages to help compile OpenCV.
```
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3-dev
```
Note that each line has to be run individually, as some packages have dependencies located in the command above it.

## Downloading OpenCV
There are 2 packages that are required for download, in order of OpenCV to run. you can grab them bun running the commands below:
```
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.2.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.4.2.zip
unzip opencv.zip
unzip opencv_contrib.zip
```
At the time of writing, version 3.4.2 is the latest version. If there is a later version, simply change the version numbers. Note that the version numbers must match for these packages to compile.

## Preparing the Python Compiler
Before we get started, we need a Python Package Manager
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py
```
The package manager is used to help maintain Python-specific packages, in the same way that the Raspbian Repository maintains software packages for the OS. One particular package we need is the Virtual Environment package and dependencies. The Virtual Envirnment enables the ability to create sandboxed environments where Python can can execute without interference from other python packages. (like having individual users on one system, where documents and such do not collide with one another).

We can install these packages like so:
```
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
```
We will also need to update the terminal profile to load these packages for quick reference. Use a terminal editor such as nano to edit the following file:
```
sudo nano ~/.profile
```
and add the following lines to the bottom of the file:
```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
Reload the terminal profile simply by running the command:
```
source ~/.profile
```
You will see the terminal load in the Python packages we installed previously.
Now we create the virtual environment. Depending what version of python you wish to run with, execute one of the following commands:
```
# Python 2.7
mkvirtualenv cv -p python2

# Python 3.5
mkvirtualenv cv -p python3
```

Upon creation of the environment, it's name (in this case is cv) will appear in parentheses as a prefix to the command entry in the terminal, which can be seen below.

**IMAGE**

If this is not the case, use the commands below to enter the virtual environment
```
source ~/.profile
workon cv
```

**workon cv** is the command that enters the environment. Prior to this, we reload the profile to ensure the virtual environment packages are loaded into the terminal.

Next we need to install NumPy, a package used for numerical processing, which will in part will allow for numerical image processing for our automated controls. (BETTER EXPAND THIS)
```
pip install numpy
```

# Compiling and Installing
Now its time for the installation. But first we need to compile the software. **Note that it will take more than an hour to successfully compile**. Before we start, make sure you are in the virtual environment
```
workon cv
```
Run the following commands to create the build file for OpenCV. Note that if you are using a different version of OpenCV than what is used in this guide, be sure to change the version numbers otherwise it will not compile.
```
cd ~/opencv-3.4.2/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.2/modules \
    -D BUILD_EXAMPLES=ON ..
```
Examine the output to ensure that Interpreter, Libraries, numpy and packages path fields of the output are pointing to the correct directories. It should look similar to the images below, depending on the Python version you are using.

**IMAGE**

Now we need to change the file swap size. the default used by Raspbian is small, and could cause compilation errors. run the command below to open up the swap file configuration file in nano:
```
sudo nano /etc/dphys-swapfile
```

Look fo rthe CONF_SWAPSIZE parameter from 100 to 1024. this will increase the swap file to 1GB. Note that we will need to change it back after compilation, as it could fill up ths SD card over time, very quickly. the parameter should now look like this:
```
CONF_SWAPSIZE=1024
```
Once this is done, we need to ensure that the chage takes effect. Run the commands below to restart the swapfile service.
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```
Now we can start the compilation. Again, be aware that the compilation process will take more than an hour to complete. you also should still be in the build directory.
```
cd ~/opencv-3.4.2/build
make -j4
```
When the compilation is complete, we can start the install onto the Pi.
```
sudo make install
sudo ldconfig
```

Lastly, execute one of the following blocks of code, depending on the version of Python you compiled with. These blocks create the symbolic link between the OpenCV packages and the virtual environment we created earlier.

```
# Python 2.7
cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so
```

```
# Python 3.5
cd /usr/local/lib/python3.5/site-packages/
sudo mv cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so

cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so
```
# Wireless Hotspot Configuration
This is mainly takes one command to fully configure using the [RaspAP Utility](https://github.com/billz/raspap-webgui). This utility installs the required dependencies and configures the Raspberry Pi into a self-serving Internet access point. The advantage to this is that it can allow connections from multiple devices and allow them 'Internet' access, like a modem would. Internet can also be passed through the RasPi via its on board ethernet port.

Before setup, disconnect any wireless networks the device may already be connected to, and plug in an ethernet cable. Execute the command below and it will download the required files and start the install.

```
wget -q https://git.io/voEUQ -O /tmp/raspap && bash /tmp/raspap
```

It will prompt you for input, accept them by typing 'y' and hitting enter (as some prompts are defaulted to 'no' when you hit enter). The Pi will need a reboot when prompted to do so. Once it has rebooted, you should see a new WiFi called ``raspi-webgui``. This is the newly configured access point. The default parameters are as below:
* SSID: raspi-webgui
* Password: ChangeMe
* IP address: 10.3.141.1
  - Login Username: admin
  - Login Password: secret
  - DHCP range: 10.3.141.50 to 10.3.141.255

You can log into the web interface, and change parameters by using the login details listed above. These are the default parameters, so you may wish to change them.


**ADD MORE HERE FOR ANY CODE DEPLOYMENT**
