# -*- coding: utf-8 -*-

import Pyro5.api


moedas = Pyro5.api.Proxy("PYRONAME:example.greeting")
