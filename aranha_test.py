#!/usr/bin/env python
from __future__ import print_function, division

# this is main script
# simple version

import aiwolfpy
import aiwolfpy.contentbuilder as cb
from random import sample

myname = 'caranha_aiwolf'

class SampleAgent(object):

    def __init__(self, agent_name):
        # myname
        self.myname = agent_name


    def getName(self):
        return self.myname

    def initialize(self, base_info, diff_data, game_setting):
        print("## INITIALIZE ##")

        self.base_info = base_info
        self.game_setting = game_setting

        self.myid = base_info["agentIdx"]
        self.talk_limit = base_info["remainTalkMap"][str(self.myid)]
        self.myrole = base_info["myRole"]

        ## Set up a list of random targets
        targets = base_info["remainTalkMap"].keys()
        self.target_list = sample(targets, len(targets))
        self.target_list.remove(str(self.myid))

        # print("First day, my id is {} and I'm a {}.".format(self.myid, self.myrole))
        print("My target list is {}".format(self.target_list))

    def update(self, base_info, diff_data, request):
        print("## UPDATE ##")
        self.base_info = base_info
        print(diff_data)
        print(request)

    def dayStart(self):
        print("## NEW DAY ##")
        # update_target list
        self.talk_n = self.talk_limit

        status = self.base_info["statusMap"]
        for i in status.keys():
            if status[i] == 'DEAD' and i in self.target_list:
                self.target_list.remove(i)

        print("New day! My target list is {}".format(self.target_list))
        return None

    def talk(self):
        print("## TALK ##")
        self.talk_n -= 1
        if self.talk_n == 9:
            return cb.vote(int(self.target_list[0]))
        else:
            return cb.over()

    def whisper(self):
        print("## WHISPER ##")
        return cb.over()

    def vote(self):
        print("## VOTE ##")
        return self.target_list[0]

    def attack(self):
        print("## ATTACK ##")
        return self.target_list[0]

    def divine(self):
        print("## DIVINE ##")
        return self.base_info['agentIdx']

    def guard(self):
        print("## GUARD ##")
        return self.base_info['agentIdx']

    def finish(self):
        print("## FINISH ##")
        return None

agent = SampleAgent(myname)



# run
if __name__ == '__main__':
    aiwolfpy.connect_parse(agent)
