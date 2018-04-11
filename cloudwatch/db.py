#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from models import CloudDb
from conf import config


class AWSdb(object):

    def __init__(self, profile, class_name):
        self.profile = profile
        self.class_name = class_name
        self.db = CloudDb()

    def insert_metric(self, dimension, mark,
                tb_name='metric_statistics', func_name='get_metric_statistics'):
        obj = self.class_name(self.profile)
        if obj.namespace == 'AWS/EC2':
            resources, time_utc = getattr(obj, func_name)(dimension, mark, startime=600, endtime=300)
        elif obj.namespace == 'AWS/ELB':
            resources, time_utc = getattr(obj, func_name)(dimension, mark)

        for resource in resources:
            if resources[resource] is None:
                data = {
                    'resource_mark': mark,
                    'metric': resource,
                    'time_utc': time_utc,
                    'resource_type': obj.namespace,
                    'profile': obj.profile
                }
            else:
                data = {
                    'resource_mark': mark,
                    'metric': resource,
                    'time_utc': time_utc,
                    'resource_type': obj.namespace,
                    'maximum': resources[resource]['Maximum'],
                    'minimum': resources[resource]['Minimum'],
                    'average': resources[resource]['Average'],
                    'sum': resources[resource]['Sum'],
                    'samplecount': resources[resource]['SampleCount'],
                    'profile': obj.profile
                }
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            sql = 'INSERT IGNORE INTO %s ( %s ) VALUES ( %s )' % (tb_name, columns, placeholders)
            self.db.sql_commit(sql, data.values())

    def insert_resource(self, tb_name, func_name):
        obj = self.class_name(self.profile)
        resources = getattr(obj, func_name)()
        for resource in resources:
            placeholders = ', '.join(['%s'] * len(resource))
            columns = ', '.join(resource.keys())
            sql = 'INSERT IGNORE INTO %s ( %s ) VALUES ( %s )' % (tb_name, columns, placeholders)
            self.db.sql_commit(sql, resource.values())

    def list_resource(self):
        obj = self.class_name(self.profile)
        namespace = obj.namespace
        if namespace == 'AWS/EC2':
            table = config.ec2_table
            field = config.ec2_primary_key
        elif namespace == 'AWS/ELB':
            table = config.elb_table
            field = config.elb_primary_key
        sql = 'SELECT %s FROM %s' % (field, table)
        ret = []
        res = self.db.sql_fetch(sql)
        for r in res:
            ret.append(r[0])
        return ret
