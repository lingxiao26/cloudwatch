#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# AWS Cloudwatch elb 统计数据的时间跟标准时间是同步的
#
import sys
from cw_space import CWSpace


class ELB(CWSpace):

    def __init__(self, profile):
        self.namespace = 'AWS/ELB'
        super(ELB, self).__init__(profile, self.namespace)
        self.profile = profile
        self.dimension = ['AvailabilityZone', 'LoadBalancerName']


if __name__ == '__main__':
    from cloudwatch.db import AWSdb
    awsdb = AWSdb('je', globals()['ELB'])
    awsdb.insert_metric('LoadBalancerName', 'df-prod')
    # marks = ['df-pre', 'dfvpc-pre', 'je-pre']
    # statistics = 'Sum'
    # for mark in marks:
    #     insert('je', globals()['ELB'], mark, 'LoadBalancerName')
        # sys.exit()
    # elb = ELB('je')
    # r = elb.get_metric_statistics('LoadBalancerName', 'df-prod')
    # print r

