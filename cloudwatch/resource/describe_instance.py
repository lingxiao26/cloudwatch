#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#

from describe_aws_resource import DescribeAwsResource


class DescribeInstances(DescribeAwsResource):
    def __init__(self, profile, region='us-east-1'):
        self.profile = profile
        super(DescribeInstances, self).__init__(profile, 'ec2', region)

    def list_instances(self):
        response = self.ec2client.describe_instances()
        reservations = response["Reservations"]
        stacks = []
        for instances in reservations:
            for instance in instances['Instances']:
                tags = instance['Tags']
                instance_id = instance['InstanceId']
                instance_status = instance['State']['Name']
                instance_type = instance['InstanceType']
                try:
                    public_ip = instance['PublicIpAddress']
                    private_ip = instance['PrivateIpAddress']
                except KeyError, e:
                    private_ip = None
                    public_ip = None
                for tag in tags:
                    if tag['Key'] == 'stack-status':
                        stack_status = tag['Value']
                    if tag['Key'] == 'aws:cloudformation:stack-name':
                        stack_name = tag['Value']
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                stack = {
                    'name': name,
                    'instance_id': instance_id,
                    'instance_status': instance_status,
                    'instance_type': instance_type,
                    'stack_name': stack_name,
                    'stack_status': stack_status,
                    'private_ip': private_ip,
                    'public_ip': public_ip,
                    'profile': self.profile
                }
                stacks.append(stack)
        return stacks

    def get_instance_by_id(self, instance_id):
        pass


if __name__ == '__main__':
    di = DescribeInstances('je')
