import imp
import unittest
from Rules import *
from Game import Game
from Mission import *
from Coder import *

class TestRules(unittest.TestCase):
    
    def test_check_nombre_coder_valid(self):
        self.assertEqual(CheckNombreCoder(1), True)
        self.assertEqual(CheckNombreCoder(4), True)

    def test_check_nombre_coder_invalid(self):
        self.assertEqual(CheckNombreCoder(0), False)
        self.assertEqual(CheckNombreCoder(5), False)

    def test_check_level_choice_valid(self):
        self.assertEqual(CheckLevelChoice("facile"), True)
        self.assertEqual(CheckLevelChoice("intermediaire"), True)
        self.assertEqual(CheckLevelChoice("difficile"), True)

    def test_check_level_choice_invalid(self):
        self.assertEqual(CheckLevelChoice("trop_facile"), False)
        self.assertEqual(CheckLevelChoice("dur"), False)
        
# Création d'une classe pour les tests

import unittest

# Ajoutez ici la fonction CheckDirectionInput


class TestCheckDirectionInput(unittest.TestCase):

    def test_valid_direction(self):
        # Test avec une direction valide
        coup_possible_coder = ['h', 'b', 'g', 'd']
        valid_direction = 'h'

        result = CheckDirectionInput(valid_direction, coup_possible_coder)

        self.assertEqual(result, True)

    def test_invalid_direction(self):
        # Test avec une direction invalide
        coup_possible_coder = ['h', 'b', 'g', 'd']
        invalid_direction = 'x'

        result = CheckDirectionInput(invalid_direction, coup_possible_coder)

        self.assertEqual(result, False)

    # Ajoutez d'autres tests si nécessaire

    
    
    # Ajoutez d'autres méthodes de test pour les autres fonctionnalités de la classe Game

if __name__ == '__main__':
    unittest.main()


