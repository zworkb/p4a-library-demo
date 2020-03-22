# P4A library demonstrator

- This code demonstrates how [python-for-android](https://github.com/kivy/python-for-android) to use a python service in a library(aar) being used by a kotlin app
- uses websockets to communicate between kotlin and python
- please build the android library first since its output is used by the kivy part

## see subprojects for further information

- [p4a-library](p4a-library/README.md) contains the python echo service pagaged as an .aar
- [kotlin activity](activity-demo/README.md) contains the AndroidStudio project that tests the echo service