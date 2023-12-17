from paralex import paralex_factory

package = paralex_factory("LeFFI",
                          {
                              "forms": {"path": "LeFFI_forms.csv",},
                              "cells": {"path": "LeFFI_cells.csv"},
                              "features-values": {"path": "LeFFI_features-values.csv"},
                              "sounds": {"path": "LeFFI_sounds.csv"},
                              "lexemes": {"path": "LeFFI_lexemes.csv"}
                          },
                          citation="Pellegrini, M. & Cignarella, A. (2023). LeFFI 2.0. Online.",
                          version="2.0",
                          keywords=["Italian", "verbs", "paradigms" , "cells"],
                          id="?",
                          contributors=[{'title': 'Matteo Pellegrini', 'role': 'author'},
						  {'title': 'Alessandra Cignarella', 'role': 'author'}],
                          licenses=[{'name': 'CC BY-SA 4.0 DEED',
                                     'title': 'Creative Commons Attribution-ShareAlike 4.0 International',
                                     'path': 'https://creativecommons.org/licenses/by-sa/4.0/'}]
)
package.to_json("LeFFI_package.json")