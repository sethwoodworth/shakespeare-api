#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from collections import OrderedDict
import os

import xmltodict

LIBRARY_PATH = './texts/texts/moby/'
DTD_PATH = os.path.join(LIBRARY_PATH, 'play.dtd')


def load_xml():
    """ Load XMl based on global LIBRARY & DTD paths"""
    play = 'romeo_and_juliet_moby.xml'
    play_path = os.path.join(LIBRARY_PATH, play)
    with open(play_path) as _file:
        xmld = xmltodict.parse(_file.read())
    return xmld


class Play(object):
    def __init__(self, xml):
        self.play = xml['PLAY']
        self.acts = [Act(act) for act in self.play['ACT']]
        self.title = self.play['TITLE']


class Act(object):
    def __init__(self, act):
        self.act = act
        self.title = self.act['TITLE']
        self.scenes = [Scene(scene) for scene in self.act['SCENE']]


class Scene(object):
    def __init__(self, scene):
        self.scene = scene
        self.title = self.scene['TITLE']
        self.stage_dir = self.scene['STAGEDIR']
        self.speeches = [Speech(speech) for speech in self.scene['SPEECH']]


class Speech(object):
    def __init__(self, speech):
        self.speech = speech
        self.speaker = self.speech['SPEAKER']
        self.lines = [line for line in self.speech['LINE']]


def list_characters(play):
    characters = OrderedDict()
    for act in play.acts:
        for scene in act.scenes:
            for speech in scene.speeches:
                speaker = speech.speaker
                character_lines = characters.get(speaker, [])
                for line in speech.lines:
                    character_lines.append(line)
                characters[speaker] = character_lines
    return characters


if __name__ == '__main__':
    x = load_xml()
    p = Play(x)
