#!/usr/bin/env python3
import os

import aws_cdk as cdk
from environments.dev import dev
# from environments.qa import qa
from kachi_cdk_demo.kachi_cdk_demo_stack import KachiCdkDemoStack


app = cdk.App()
KachiCdkDemoStack(app, "KachiCdkDemoStackDev",config=dev)
# KachiCdkDemoStack(app, "KachiCdkDemoStackqa",config=qa)

app.synth()
