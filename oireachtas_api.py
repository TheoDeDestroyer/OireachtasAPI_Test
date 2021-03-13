#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Set of functions to query the Oireachtas api at
https://api.oireachtas.ie/v1/
"""
import json
import os
from json import *
from datetime import *
import requests
import time
start_time = time.time()

LEGISLATION_DATASET = 'legislation.json'
MEMBERS_DATASET = 'members.json'

load = lambda jfname: loads(open(jfname, encoding="utf8").read())


def filter_bills_sponsored_by(pId):
    """Return bills sponsored by the member with the specified pId

    :param str pId: The pId value for the member
    :return: dict of bill records
    :rtype: dict
    """
    # leg = load(LEGISLATION_DATASET)
    # mem = load(MEMBERS_DATASET)
    legislation_ref = requests.get("https://api.oireachtas.ie/v1/legislation").json()
    leg = json.dumps(legislation_ref)
    print(leg)
    members_ref = requests.get("https://api.oireachtas.ie/v1/members").json()
    mem = json.dumps(members_ref)
    ret = []
    for res in leg['results']:
        p = res['bill']['sponsors']
        for i in p:
            name = i['sponsor']['by']['showAs']
            for result in mem['results']:
                fname = result['member']['fullName']
                rpId = result['member']['pId']
                if fname == name and rpId == pId:
                    ret.append(res['bill'])
    print(ret)
    print("API Run time: ", time.time() - start_time)
    return ret


if __name__ == '__main__':
    filter_bills_sponsored_by('IvanaBacik')


def filter_bills_by_last_updated(since, until):
    """Return bills updated within the specified date range

    :param datetime.date since: The lastUpdated value for the bill
        should be greater than or equal to this date
    :param datetime.date until: The lastUpdated value for the bill
        should be less than or equal to this date. If unspecified, until
        will default to today's date
    :return: List of bill records
    :rtype: list

    """
    raise NotImplementedError
