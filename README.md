behavior-engine
===============

BehaviorEngine is simple, experimental engine for implementing logic
in a Raspberry Pi-based robot.

Background
----------

I am planning to build a RPi robot and it needs some brains. 
Generic, behavior-based engine sounds like a promising starting point. 

I took the basic idea for the engine from [here](http://lejos.sourceforge.net/nxt/nxj/tutorial/Behaviors/BehaviorProgramming.htm).
I modified the concept by giving each behavior access to the behavior engine
(called Arbitrator in the leJOS).

Requirements
------------

The test code is written using Quick2Wire Python library. To run the test code
you need to install
* [quick2wire-gpio-admin](https://github.com/quick2wire/quick2wire-gpio-admin)
* [quick2wire-python-api](https://github.com/quick2wire/quick2wire-python-api)



