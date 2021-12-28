# !/usr/bin/env python
# -*- coding=utf-8 -*-
"""
The script is used to make data
command: python manage.py make_data
"""
import logging
import json, time, datetime
from django.core.management.base import BaseCommand
from django.conf import settings as conf


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.run()

    def run(self):
        """
        造数据
        :return:None
        """
        self.make_data()

    def make_data(self):
        try:
            pass
        except Exception as e:
            pass
