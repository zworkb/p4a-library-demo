[app]

# (str) Title of your application
title = Kivy native UI Demo

# (str) Package name
package.name = kivynativeactivity

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png
source.include_patterns = res/*

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3, websockets

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
services = websockets:service.py

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 28

# (int) Minimum API your APK will support.
android.minapi = 23

# (int) Android SDK version to use
android.sdk = 28

# (str) Android NDK version to use
#android.ndk = 17c

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True


# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = armeabi-v7a
android.arch = arm64-v8a

#
# Python for android (p4a) specific
#

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
p4a.source_dir = ~/p4a
#p4a.source_dir = ~/p4a_aar

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
p4a.bootstrap = library

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port =



[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
