aws-user-management
=========

This role is to manage AWS IAM users and groups and associate existing IAM policies with them.

Requirements
------------

Same as the underlying modules:

* boto
* boto3
* botocore
* python >= 2.6

Currently only support the external setting of the API keys or profile and AWS region.

Role Variables
--------------

iam_users: List of IAM users to create. *User deletion still needs to be developed.*
iam_groups: List of configurations for IAM groups.
iam_groups[].name: Name of the IAM group.
iam_groups[].policies: List of existing IAM policies to be associated with the IAM group.
iam_groups[].users: List of users to be added to the group.

Dependencies
------------

nil

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
      - role: mikhailadvani.aws-user-management
        iam_users:
          - user1
          - user2
        iam_groups:
          - name: group1
            policies:
              - arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess
              - arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
            users:
              - user1
          - name: group2
            policies:
              - arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
            users:
              - user1
              - user2


License
-------

Apache
