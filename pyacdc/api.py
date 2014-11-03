#!/bin/python
# -*- coding: utf-8 -*-

import constraints as c
from api_key import key

import requests


def __prepare_session():
    """
        Prepare the headers of the session
    """
    session = requests.Session()
    session.verify = False
    session.headers.update(
        {'Authorization': 'Token token={}'.format(key),
         'content-type': 'application/json'})
    return session


def get_ip(ip):
    session = __prepare_session()
    response = session.get('{}/api/v1/{}/{}' .format(c.url, 'ips', ip))
    return response.json()


def get_asn(asn):
    session = __prepare_session()
    response = session.get('{}/api/v1/{}/{}' .format(c.url, 'asns', asn))
    return response.json()


def get_domain(domain):
    session = __prepare_session()
    response = session.get('{}/api/v1/{}/{}' .format(c.url, 'domains', domain))
    return response.json()


def get_report(report):
    session = __prepare_session()
    response = session.get('{}/api/v1/{}/{}' .format(c.url, 'reports', report))
    return response.json()
