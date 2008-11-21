"This module collects algorithms and utility functions operating on UFL objects."

__authors__ = "Martin Sandve Alnes"
__date__ = "2008-08-14 -- 2008-11-21"

# Modified by Anders Logg, 2008

# Utilities for traversing over expression trees in different ways
from ufl.algorithms.traversal import iter_expressions, traverse_terminals, \
                                     post_traversal, pre_traversal, traversal, \
                                     post_walk, pre_walk, walk

# Utilities for extracting information from forms and expressions
from ufl.algorithms.analysis import extract_classes, extract_type, \
                                    extract_basisfunctions, extract_coefficients, \
                                    extract_elements, extract_unique_elements, \
                                    extract_variables, extract_duplications
from ufl.algorithms.monomials import extract_monomials

# Utility class for easy collecting of data about form
from ufl.algorithms.formdata import FormData

# Utilities for checking properties of forms
from ufl.algorithms.predicates import is_multilinear

# Utilities for error checking of forms
from ufl.algorithms.checks import validate_form

# Utilites for modifying expressions and forms
from ufl.algorithms.transformations import transform, transform_integrands, \
                                           ufl2ufl, ufl2uflcopy, \
                                           replace, flatten, strip_variables, \
                                           expand_compounds, mark_duplications

# Utilities for working with dependencies of subexpressions
from ufl.algorithms.dependencies import split_by_dependencies

# Utilities for transforming complete Forms into other Forms
from ufl.algorithms.formtransformations import compute_form_adjoint, compute_form_action, \
                                               compute_form_lhs, compute_form_rhs #, compute_dirichlet_functional

# Utilities for Automatic Functional Differentiation
from ufl.algorithms.ad import compute_diff, propagate_spatial_derivatives, compute_form_derivative

# Utilities for UFL object printing
from ufl.algorithms.printing import integral_info, form_info, tree_format
from ufl.algorithms.ufl2latex import ufl2latex, ufl2tex, ufl2pdf
from ufl.algorithms.ufl2dot import ufl2dot

# Utilities for form file handling
from ufl.algorithms.formfiles import load_forms
