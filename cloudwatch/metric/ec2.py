#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# AWS Cloudwatch ec2的统计数据时间比标准时间晚10min（utc time）
import sys
from cw_space import CWSpace


class EC2(CWSpace):

    def __init__(self, profile):
        self.namespace = 'AWS/EC2'
        super(EC2, self).__init__(profile, self.namespace)
        self.profile = profile
        self.dimension = ['ImageId', 'InstanceId', 'InstanceType']


if __name__ == '__main__':
    from cloudwatch.db import AWSdb
    awsdb = AWSdb('je', globals()['EC2'])
    awsdb.insert_metric('InstanceId', 'i-01668ae70eb3b300d')
    # from store2db import insert
    # marks = ['i-00d1a2668704cbee6', 'i-01668ae70eb3b300d']
    # for mark in marks:
    #     insert('je', globals()['EC2'], mark, 'InstanceId')
        # sys.exit()
    # data, time_utc = EC2('je').get_metric_statistics('InstanceId', 'i-00d1a2668704cbee6', startime=600, endtime=300)
    # print data
    # print time_utc

