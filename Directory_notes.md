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
* this must read config files from storage, as more routines/tasks will be added by the users
### Questions
* Should this pass the Cameras to a given routine/task or should the routines themselves grab the associated cameras
* 
# Storage
## Configs
### Cameras
* this directory contains Config files for the Cameras, such as their directory location (i.e. `/dev/video0, /dev/video1`) for webcams or urls for ip cams
* may contain some kind of designation(living room, front door), if so could replace need for routines as the event handler or the task could grab all cameras with a given designation
* may make more sense to store in a database if so, IDK
### Tasks/Routines
* these are list of cameras to use for a given task/routine
* these configs could completely replace the routines, 
## Database
database for users should contain:
* the name of the user
* perhaps a designation(primary user, friend,employee, shoplifter, etc)
* a (relative or absolute) path to the facial embeddings associated with that name
## Models
* this directory contains the models necessary for all the tasks
* should probably either be completely added to git ignore, or the embedded directories should be ignored and the only file in here is a download script, though that may make more sense to put somewhere else(wherever new tasks are added)
### Face_detection
* model(s) for face detection
## FaceData
### UserPhotos
* these are directorys containing approximately 20 photos collected for each person who needs to be recognized
* each directory in here is named after the user
* not sure if friendly users should be in a separate directory from people who should be recognized but aren't people who the primary user would consider friendly
* it may make more sense to leave that up to the database, assigning each named person a designation
### UserEmbeddings
* these are the facial embeddings that the facial recognition task uses to identify that particular user
