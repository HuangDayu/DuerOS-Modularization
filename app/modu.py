# -*- coding: utf-8 -*-

import wakeup_trigger_main

while True:
    if wakeup_trigger_main.getText() != "":
        print(wakeup_trigger_main.getText())
    else:
        pass