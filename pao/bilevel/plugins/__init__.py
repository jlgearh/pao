#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright 2017 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and 
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain 
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

def load():
    import pyomo.bilevel.plugins.dual
    import pyomo.bilevel.plugins.lcp
    import pyomo.bilevel.plugins.solver1
    import pyomo.bilevel.plugins.solver2
    import pyomo.bilevel.plugins.solver3
    import pyomo.bilevel.plugins.solver4