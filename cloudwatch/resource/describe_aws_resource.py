#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import boto3


class DescribeAwsResource(object):

    def __init__(self, profile, resource, region='us-east-1'):
        self.profile = profile
        self.session = boto3.Session(profile_name=self.profile)
        self.client = self.session.client(resource, region_name=region)