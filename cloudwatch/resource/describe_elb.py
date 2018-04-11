#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# from datetime import datetime
from describe_aws_resource import DescribeAwsResource


class DescribeElb(DescribeAwsResource):

    def __init__(self, profile, region='us-east-1'):
        self.profile = profile
        super(DescribeElb, self).__init__(profile, 'elb', region)

    def list_elb(self):
        elbs = []
        response = self.client.describe_load_balancers()
        for elb in response['LoadBalancerDescriptions']:
            elb_name = elb['LoadBalancerName']
            created_time = elb['CreatedTime'].strftime('%Y-%m-%d %H:%M:%S')
            instances = ', '.join([i['InstanceId'] for i in elb['Instances']])
            elbs.append({
                'elb_name': elb_name,
                'created_time': created_time,
                'instances': instances,
                'profile': self.profile
            })
        return elbs

if __name__ == '__main__':
    pass
    # de = DescribeElb('je')
    # elbs = de.list_elb()
    # from store2db import insert
    # insert('je', 'elb_gallery', globals()['DescribeElb'], 'list_elb')

