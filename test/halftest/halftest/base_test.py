"""Base test class for the halftest package.

This class is inherited by every test modules in the package.
"""

from unittest import TestCase
from half_orm.relation import Relation

#>>> PLACE YOUR CODE BELOW THIS LINE. DO NOT REMOVE THIS LINE!


#<<< PLACE YOUR CODE ABOVE THIS LINE. DO NOT REMOVE THIS LINE!


class BaseTest(TestCase):
    #>>> PLACE YOUR CODE BELOW THIS LINE. DO NOT REMOVE THIS LINE!


    #<<< PLACE YOUR CODE ABOVE THIS LINE. DO NOT REMOVE THIS LINE!


    def setUp(self) -> None:
        self.Relation = Relation
        #>>> PLACE YOUR CODE BELOW THIS LINE. DO NOT REMOVE THIS LINE!


        #<<< PLACE YOUR CODE ABOVE THIS LINE. DO NOT REMOVE THIS LINE!


    def tearDown(self) -> None:
        pass
        #>>> PLACE YOUR CODE BELOW THIS LINE. DO NOT REMOVE THIS LINE!

