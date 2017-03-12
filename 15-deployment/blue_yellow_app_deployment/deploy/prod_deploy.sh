#!/bin/bash
ansible-playbook -vvvv ./deploy.yml --private-key=/home/matt/do_deploy -u deployer -i ./hosts
