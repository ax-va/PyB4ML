from bayesian.modeling.node import Node


class Variable(Node):
    def __init__(self, domain, name=None):
        self._domain = domain
        self._linked_factors = []
        Node.__init__(self, name)

    @property
    def domain(self):
        return self._domain

    @property
    def factors(self):
        return self._linked_factors

    @property
    def name(self):
        return self._name

    def is_isolated_leaf(self):
        return len(self._linked_factors) == 0

    def is_non_isolated_leaf(self):
        return len(self._linked_factors) == 1

    def link_factor(self, factor):
        self._linked_factors.append(factor)
