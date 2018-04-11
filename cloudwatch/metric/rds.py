#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from cw_space import CWSpace


class RDS(CWSpace):

    def __init__(self, profile):
        self.namespace = 'AWS/RDS'
        super(RDS, self).__init__(profile, self.namespace)
        self.profile = profile
        self.dimension = ['DBInstanceIdentifier', 'DBClusterIdentifier', 'DatabaseClass']


if __name__ == '__main__':
    elb = RDS('je')
    # metrics = elb.get_metrics()
    # print metrics
    sta_data, metric = elb.get_metric_statistics('InstanceId', 'i-00d1a2668704cbee6')
    print sta_data
    print metric

