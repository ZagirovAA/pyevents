#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ObjectWithEvents:

    callbacks = None

    def addEvent(self, eventname, callback):
        if self.callbacks is None:
            self.callbacks = {}
        if eventname not in self.callbacks:
            self.callbacks[eventname] = [callback]
        else:
            self.callbacks[eventname].append(callback)

    def delEvent(self, eventname, callback):
        if self.callbacks is not None and eventname in self.callbacks:
            if callback in self.callbacks[eventname]:
                self.callbacks[eventname].remove(callback)

    def triggerEvent(self, eventname):
        if self.callbacks is not None and eventname in self.callbacks:
            for callback in self.callbacks[eventname]:
                callback()
