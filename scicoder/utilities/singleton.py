#!/usr/bin/python

'''
This function implements the singleton design pattern in Python.
To use it, simply import this file:

from singleton import singleton

and declare your class as such:

@singleton
class A(object):
	pass
'''

def singleton(cls):
    instance_container = []
    def getinstance():
        if not len(instance_container):
            instance_container.append(cls())
        return instance_container[0]
    return getinstance