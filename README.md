# PUPPA
*Python UPdating Package Application*
* * *
 
An updatable application package made with Python.

** WARNING! This software is experimental. It's lazy and carefree! To be used with caution! **

## Requirements

* [Python 2.7.x](https://www.python.org/downloads/)

## Installation
1. Dowload the first distribution from [dist/puppa](https://github.com/jonathanargentiero/puppa/blob/0.1/dist/puppa?raw=true).
2. Copy it wherever you like.

## How to use
* Run on the command line:   
   (if you have done step 3)
   
   ````
   $ cd /my/path/to/
   $ python puppa -v
   ````
   
   (or)
   
   ````
   $ python /my/path/to/puppa -v
   ````
   
   If everything is fine you will be given this output:
   
   ````
   $ python puppa -v   
     v0.1
   ````   
   
* Now update to the latest version:
   
   ````
   $ python puppa update
   $ python puppa -v   
     v0.3
   ````
   
* Update to a specific version:
   
   ````
   $ python puppa update 0.2
   $ python puppa -v   
     v0.2
   ````
   
* Purge the puppa:
   
   ````
   $ python puppa purge
   ````

## Commands

In the command line run:

````
$ python puppa --help
````

to see a list of the enabled commands like:

````
$ python puppa --version
$ python puppa --path
$ python puppa --help
$ python puppa update 
$ python puppa purge
````

## How to create a puppa package

1. Download the sources
2. Make your modifications
3. Zip (yes, just `$ zip` or winzip) everything except for `/dist` folder
4. Rename `puppa.zip` to `puppa` (remove the extension)
5. Update the `puppa` file on your repository

## How to configure your own puppa

* check `lib/manager.py` for configuration settings
* remove lines under `optional versioning based on Github` from `lib/update.py` if you won't use Github

## Help

This project is discussed on [this blog post](http://blog.jonathanargentiero.com/puppa)

## Contribute

The project is just a POC. You can contribute by making pull-requests to the repository, but it could be a waste of your precious time.