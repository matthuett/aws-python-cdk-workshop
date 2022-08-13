#!/usr/bin/env python3

import aws_cdk as cdk

from tutorial.tutorial_stack import TutorialStack


app = cdk.App()
TutorialStack(app, "tutorial")

app.synth()
