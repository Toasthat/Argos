# Frontend
## Gui
Allow a user to configure the initial app, maybe 
### What it needs so far
#### ON initial Configuration
* Allow user to sign in to google
# Source
## backend_ports
## frontend_ports
## Routines
* These are collections of tasks that are to be executed sequentially
* they may not be necessary, as this idea was developed before I realized that facial detection was separate for facial recognition, and I thought that in order to avoid heavy resource usage(constantly trying to recognize faces that aren't there) motion detection was a necessary prerequisite.
* If this is the case it may make more sense to pass the feeds directly to the tasks, and use the event handler to handle what to do on a given event(face detected, not user, upload to drive)
* it still makes sense to make task modular classes because there is a lot of overlap with computer vision tasks and we could reuse a lot of code amongst the computer vision stuff
### Tasks
* these are the things that actually do the computer vision stuff
## Sentinel
This is a c++ daemon that monitors for "events" i.e. triggers that are defined in the routines, and then starts the routines associated with that trigger
### Example 
User walks in the out the front door, and this causes the routine that catches this to send some kind of message to Sentinel, which then starts the security routine
### Requirements
* this must use the minimum amount of CPU time possible, perhaps putting in some kind of `wait` command in the main loop
* this must be able to run 24/7 without crashing(I've had bad experiences with similar projects in python after a day or so)
* this must read config files from storage, as more routines will be added by the users
### Questions
* Should this pass the Cameras to a given routine/task or should the routines themselves grab the associated cameras
* 
# Storage
## Configs
### Cameras
*this directory contains Config files for the Cameras, su
###
## Database
## Models
### Face_detection
## FaceData
### UserPhotos
### Facial Embeddings
