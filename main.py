#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from cloudwatch.metric.ec2 import EC2
from cloudwatch.metric.elb import ELB
from cloudwatch.db import AWSdb
from conf import config


class Main(object):

    def __init__(self, profile, mark):
        """
        :param profile: 'je'|'js'|'hd'|'jt'
        :param mark: 'EC2'|'ELB'|'RDS'|...
        :return: list of resource
        """
        self.profile = profile
        self.mark = mark
        self.aws_db = AWSdb(self.profile, globals()[self.mark])
        if self.mark == 'Ec2':
            self.dimention = config.ec2_dimention
        elif self.mark == 'ELB':
            self.dimention = config.elb_dimention

    def list_resource(self):
        return self.aws_db.list_resource()

    def insert_metric(self):
        resouces = self.list_resource()
        for r in resouces:
            self.aws_db.insert_metric(self.dimention, r)


if __name__ == '__main__':
    m = Main('je', 'EC2')