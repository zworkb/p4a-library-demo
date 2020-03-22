# Android library demonstrator

## Activity

This is a simple Activity that communicates via websockets with the Python backend

## Setup

- Android Studio 3.6+
- Kotlin 1.3.60
- ktor websockets client

### project setup

First compile the [p4a-library](../p4a_library),
then you can open this directory in AndroidStudio and compile/run it. 

the following steps have been done to the default project:

#### build.gradle
- add ktor version string
- add repo maven { url 'https://kotlin.bintray.com/ktor' }
- add ktor deps for core, websockets, cio
    
    gives error "More than one file was found with OS independent path 'META-INF/ktor-http.kotlin_module'"

    - this is solved by adding the block to the android section:
        packagingOptions {
        // see https://stackoverflow.com/questions/56484281/compiler-cannot-resolve-classes-in-io-ktor-client-features-logging
        exclude 'META-INF/common.kotlin_module'
        exclude 'META-INF/*.kotlin_module'
    }

#### AndroidManifest.xml

- add INTERNET permission to the Manifest
