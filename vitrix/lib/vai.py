# CREATED AND MAINTAINED BY SANDIPAN GUHA ON 26-4-22
# EXPERIMENTAL V1.0
'''
THE BASIC IDEA BEHIND THIS IS TO MINIMIZE THE CODING EFFORT FOR DEVELOPERS AND CONTRIBUTORS AND MAXIMIZE THE CODE DISCIPLINE.
AI CONCEPT USED IN THIS PROJECT IS VERY SIMPLE AND EASY TO USE BY ANYONE. THE CORE MECHANICS IS BASED ON BEHAVIOURAL TREE SYSTEM AND
INTENDS TO DO SO IN THE FUTURE.
'''
from ursina import *

class VAI():
    #class atributes
    _version = 1.0
    _desc = "Vitrix AI is a easy to use game AI system using Behavioural Trees method. "
    _status = None
    def __init__(self,friend=False,target=None,leader=None) -> None:
        _friendly = friend
        _target = target
        _leader = leader
    

    def update(self):
        if self._target==None:
            self.wander(self._leader)
        else:
            self.pathfind(self._target)
        #if target in vicinity shoot the target or attack him
        #if object is friendly dont attack

    def wander(self,_leader):
        pass
    def pathfind(self,_target):
        pass
    def status():
        pass

