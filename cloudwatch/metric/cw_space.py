#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import boto3
import ssl
from datetime import datetime, timedelta


class CWSpace(object):

    def __init__(self, profile, namespace, region='us-east-1'):
        self.namespace = namespace
        self.profile = profile
        self.session = boto3.Session(profile_name=self.profile)
        self.client = self.session.client('cloudwatch', region_name=region)
        self.metrics = self.get_metrics()
        self.statistics = ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum']

    def get_metrics(self):
        try:
            ret = self.client.list_metrics(Namespace=self.namespace)
        except ssl.SSLError, e:
            ret = self.client.list_metrics(Namespace=self.namespace)
        metrics = []
        for metric in ret['Metrics']:
            metrics.append(metric['MetricName'])
        return list(set(metrics))

    def get_metric_statistics(self, dimension, value, startime=60, endtime=-240):
        data = {}
        time_utc = None
        for metric in self.metrics:
            data[metric] = {}
            ret = self.client.get_metric_statistics(
                Namespace=self.namespace,
                MetricName=metric,
                Dimensions=[
                    {
                        'Name': dimension,
                        'Value': value
                    },
                ],
                StartTime=datetime.utcnow() - timedelta(seconds=startime),
                EndTime=datetime.utcnow() - timedelta(seconds=endtime),
                Period=300,
                Statistics=self.statistics
            )
            ret = ret['Datapoints']
            if len(ret) == 0:
                data[metric] = None
            else:
                for st in self.statistics:
                    data[metric][st] = ret[0][st]
                time_utc = ret[0]['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        return data, time_utc
