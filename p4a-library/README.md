# python service as aar library

## setup

- clone p4a from [zworkb android-library fork](https://github.com/zworkb/python-for-android/tree/android-library)
- clone buildozer from [zworkb android-library fork](https://github.com/zworkb/buildozer/tree/android-library)
- build the p4a-library

## build


### buildozer.spec

the following steps have been done to the `buildozer.spec` file:

- set the correct `p4a` directory (depends on your p4a location):

    p4a.source_dir = /home/phil/p4a

- set package and app name
- add `websockets` to the requirements
- register `service.py` in the services: 
    
    services = websockets:service.py

- add INTERNET permission
- android-api:18, android-minapi:23, android.sdk:28

### compile

in the root directory of the p4a-library:

    $ buildozer android debug